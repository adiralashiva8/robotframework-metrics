from robot.api import ResultVisitor


class KeywordResults(ResultVisitor):

    def __init__(self, soup, tbody, ignore_lib, ignore_type):
        self.test = None
        self.soup = soup
        self.tbody = tbody
        self.ignore_library = ignore_lib
        self.ignore_type = ignore_type

    def start_test(self, test):
        self.test = test

    def end_test(self, test):
        self.test = None

    def start_keyword(self, kw):
        # Get test case name (Credits: Robotframework author - Pekke)
        test_name = self.test.name if self.test is not None else ''

        # Ignore library keywords
        keyword_library = kw.libname

        if any(library in keyword_library for library in self.ignore_library):
            pass
        else:
            keyword_type = kw.type
            if any(library in keyword_type for library in self.ignore_type):
                pass
            else:
                table_tr = self.soup.new_tag('tr')
                self.tbody.insert(1, table_tr)

                table_td = self.soup.new_tag('td', style="word-wrap: break-word;max-width: 250px; white-space: normal")

                if keyword_type != "kw":
                    table_td.string = str(kw.parent)
                else:
                    table_td.string = str(test_name)
                table_tr.insert(0, table_td)

                table_td = self.soup.new_tag('td', style="word-wrap: break-word;max-width: 250px; white-space: normal")
                table_td.string = str(kw.kwname)
                table_tr.insert(1, table_td)

                kw_status = str(kw.status)
                if kw_status == "PASS":
                    table_td = self.soup.new_tag('td', style="color: green")
                    table_td.string = kw_status
                else:
                    table_td = self.soup.new_tag('td', style="color: red")
                    table_td.string = kw_status

                table_tr.insert(2, table_td)

                table_td = self.soup.new_tag('td')
                table_td.string = str(kw.elapsedtime / float(1000))
                table_tr.insert(3, table_td)