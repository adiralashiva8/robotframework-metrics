from robot.api import ResultVisitor


class SuiteResults(ResultVisitor):

    def __init__(self, soup, tbody, log_name):
        self.soup = soup
        self.tbody = tbody
        self.log_name = log_name

    def start_suite(self, suite):
        suite_test_list = suite.tests
        if not suite_test_list:
            pass
        else:
            stats = suite.statistics
            table_tr = self.soup.new_tag('tr')
            self.tbody.insert(0, table_tr)

            table_td = self.soup.new_tag('td',
                                    style="word-wrap: break-word;max-width: 250px; white-space: normal;cursor: pointer; text-decoration: underline; color:blue")
            table_td.string = str(suite)
            table_td['onclick'] = "openInNewTab('%s%s%s','%s%s')" % (self.log_name, '#', suite.id, '#', suite.id)
            table_td['data-toggle'] = "tooltip"
            table_td['title'] = "Click to view '%s' logs" % suite
            table_tr.insert(0, table_td)

            suite_status = str(suite.status)
            if suite_status == "PASS":
                table_td = self.soup.new_tag('td', style="color: green")
                table_td.string = suite_status
            else:
                table_td = self.soup.new_tag('td', style="color: red")
                table_td.string = suite_status

            table_tr.insert(1, table_td)

            table_td = self.soup.new_tag('td')
            table_td.string = str(stats.all.total)
            table_tr.insert(2, table_td)

            table_td = self.soup.new_tag('td')
            table_td.string = str(stats.all.passed)
            table_tr.insert(3, table_td)

            table_td = self.soup.new_tag('td')
            table_td.string = str(stats.all.failed)
            table_tr.insert(4, table_td)

            table_td = self.soup.new_tag('td')
            table_td.string = str(suite.elapsedtime / float(1000))
            table_tr.insert(5, table_td)
