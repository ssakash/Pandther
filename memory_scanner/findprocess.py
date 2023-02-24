import volatility.plugins.common as common
import volatility.utils as utils
import sys


process = sys.argv[1]
class ProcessListPlugin(common.AbstractWindowsCommand):
    """Find all processes starting with 'a'"""
    def calculate(self):
        addr_space = utils.load_as(self._config)

        for proc in self.filter_processes(addr_space):
            if proc.ImageFileName.lower().startswith(process):
                yield (0, [proc.UniqueProcessId, proc.ImageFileName])

    def render_text(self, outfd, data):
        self.table_header(outfd, [("PID", "<6"), ("Process Name", "<20")])

        for pid, name in data:
            self.table_row(outfd, [pid, name])

