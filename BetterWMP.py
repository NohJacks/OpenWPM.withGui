import argparse
from pathlib import Path
from typing import Literal

from custom_command import LinkCountingCommand
from openwpm.command_sequence import CommandSequence
from openwpm.commands.browser_commands import GetCommand
from openwpm.config import BrowserParams, ManagerParams
from openwpm.storage.sql_provider import SQLiteStorageProvider
from openwpm.task_manager import TaskManager

import date_manament

class WMPcrawler:

    def __init__(self, name, sitelist):
        self.sites = sitelist
        self.name = name
        self.display_mode: Literal["native", "headless", "xvfb"] = "native"
        # display mode "headless" means that the browser inst showen but runs in the background
        self.display_mode = "headless"
        self.load_params()
        #here the path is defined. ive made it so that the file name is equal to "name"
        self.configure_taskmanager("./datadir/", "./datadir/openwpm.log", "./datadir/{}.sqlite".format(self.name))

    def load_params(self, NUM_BROWSERS=2):
        # Loads the default ManagerParams
        # and NUM_BROWSERS copies of the default BrowserParams
        NUM_BROWSERS = 2
        self.manager_params = ManagerParams(num_browsers=NUM_BROWSERS)
        self.browser_params = [BrowserParams(display_mode=self.display_mode) for _ in range(NUM_BROWSERS)]

        # Update browser configuration (use this for per-browser settings)
        for browser_param in self.browser_params:
            # Record HTTP Requests and Responses
            browser_param.http_instrument = True
            # Record cookie changes
            browser_param.cookie_instrument = True
            # Record Navigations
            browser_param.navigation_instrument = True
            # Record JS Web API calls
            browser_param.js_instrument = True
            # Record the callstack of all WebRequests made
            # browser_param.callstack_instrument = True
            # Record DNS resolution
            browser_param.dns_instrument = True
            # Set this value as appropriate for the size of your temp directory
            # if you are running out of space
            browser_param.maximum_profile_size = 50 * (10**20)  # 50 MB = 50 * 2^20 Bytes

    def configure_taskmanager(self, datadir, logpath, storagepath):
        # Update TaskManager configuration (use this for crawl-wide settings)
        self.manager_params.data_directory = Path(datadir)
        self.manager_params.log_path = Path(logpath)
        self.storage_path = Path(storagepath)

        # memory_watchdog and process_watchdog are useful for large scale cloud crawls.
        # Please refer to docs/Configuration.md#platform-configuration-options for more information
        # manager_params.memory_watchdog = True
        # manager_params.process_watchdog = True

    def run(self):
        # Commands time out by default after 60 seconds
        with TaskManager(
            self.manager_params,
            self.browser_params,
            SQLiteStorageProvider(self.storage_path),
            None,
        ) as manager:
            # Visits the sites
            for index, site in enumerate(self.sites):

                def callback(success: bool, val: str = site) -> None:
                    print(
                        f"CommandSequence for {val} ran {'successfully' if success else 'unsuccessfully'}"
                    )

                # Parallelize sites over all number of browsers set above.
                command_sequence = CommandSequence(
                    site,
                    site_rank=index,
                    callback=callback,
                )

                # Start by visiting the page
                command_sequence.append_command(GetCommand(url=site, sleep=3), timeout=60)
                # Have a look at custom_command.py to see how to implement your own command
                command_sequence.append_command(LinkCountingCommand())

                # Run commands across all browsers (simple parallelization)
                manager.execute_command_sequence(command_sequence)

if __name__ == '__main__':
    #here the website is chosen from the veribale "sitelist" and named after "name"
    crawler = WMPcrawler('Test1', ['http://www.dr.dk'])
    crawler.run()
    #runs date_manament.py and sends over the txt file
    date_manament.main('{}'.format(crawler.name))