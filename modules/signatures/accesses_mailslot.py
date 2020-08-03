# Copyright (C) 2020 bartblaze
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from lib.cuckoo.common.abstracts import Signature

class AccessesMailslot(Signature):
    name = "accesses_mailslot"
    description = "Performs a Mailslot ping, used to get Domain Controller information"
    severity = 0.5
    categories = ["discovery"]
    authors = ["bartblaze"]
    minimum = "1.2"
    evented = True
    references = ["https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-adts/2cff75a9-5871-4493-a704-017b506f8df0"]

    def run(self):
        indicators = [
            "\\\\MAILSLOT\\\\NET\\\\NETLOGON$",
        ]

        for indicator in indicators:
            match = self.check_file(pattern=indicator, regex=True)
            if match:
                self.data.append({"file": match})
                return True

        return False
