from robot.api import ResultVisitor


class TestResults(ResultVisitor):

    def __init__(self, soup, tbody, logname):
        self.soup = soup
        self.tbody = tbody
        self.log_name = logname

    def visit_test(self, test):
        table_tr = self.soup.new_tag('tr')
        self.tbody.insert(0, table_tr)

        table_td = self.soup.new_tag('td', style="word-wrap: break-word;max-width: 200px; white-space: normal")
        table_td.string = str(test.parent)
        table_tr.insert(0, table_td)

        table_td = self.soup.new_tag('td',
                                style="word-wrap: break-word;max-width: 250px; white-space: normal;cursor: pointer; text-decoration: underline; color:blue")
        table_td.string = str(test)
        table_td['onclick'] = "openInNewTab('%s%s%s','%s%s')" % (self.log_name, '#', test.id, '#', test.id)
        table_td['data-toggle'] = "tooltip"
        table_td['title'] = "Click to view '%s' logs" % test
        table_tr.insert(1, table_td)

        table_td = self.soup.new_tag('td')
        table_td.string = str(test.status)
        table_tr.insert(2, table_td)

        table_td = self.soup.new_tag('td')
        table_td.string = str(test.elapsedtime / float(1000))
        table_tr.insert(3, table_td)