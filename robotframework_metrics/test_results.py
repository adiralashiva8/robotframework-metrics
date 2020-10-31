from robot.api import ResultVisitor


class TestResults(ResultVisitor):

    def __init__(self, soup, tbody, logname, full_suite_name, showtags):
        self.soup = soup
        self.tbody = tbody
        self.log_name = logname
        self.full_suite_name = full_suite_name
        self.showtags = showtags

    def visit_test(self, test):
        table_tr = self.soup.new_tag('tr')
        self.tbody.insert(0, table_tr)

        table_td = self.soup.new_tag('td', style="word-wrap: break-word;max-width: 200px; white-space: normal; text-align:left")
        if self.full_suite_name == "True":
            try:
                full_suite_name = test.longname.split("." + test.name)
                table_td.string = str(full_suite_name[0])
            except Exception as e:
                table_td.string = str(test.parent)
        else:
            table_td.string = str(test.parent)
        table_tr.insert(0, table_td)

        table_td = self.soup.new_tag('td', style="word-wrap: break-word;max-width: 250px; white-space: normal;cursor: pointer; color:blue; text-align:left")
        table_td.string = str(test)
        table_td['onclick'] = "openInNewTab('%s%s%s','%s%s')" % (self.log_name, '#', test.id, '#', test.id)
        table_td['data-toggle'] = "tooltip"
        table_td['title'] = "Click to view '%s' logs" % test
        table_tr.insert(1, table_td)

        test_status = str(test.status)
        if test_status == "PASS":
            table_td = self.soup.new_tag('td', style="color: green")
            table_td.string = test_status
        elif test_status == "FAIL":
            table_td = self.soup.new_tag('td', style="color: red")
            table_td.string = test_status
        else:
            table_td = self.soup.new_tag('td', style="color: orange")
            table_td.string = test_status
        table_tr.insert(2, table_td)

        table_td = self.soup.new_tag('td')
        table_td.string = str(test.elapsedtime / float(1000))
        table_tr.insert(3, table_td)

        table_td = self.soup.new_tag('td', style="word-wrap: break-word;max-width: 250px; white-space: pre-wrap;text-align:left")
        table_td.string = test.message
        table_tr.insert(4, table_td)

        if self.showtags == "True":
            table_td = self.soup.new_tag('td', style="word-wrap: break-word;max-width:100px; white-space: pre-wrap;text-align:left")
            table_td.string = str(test.tags)
            table_tr.insert(5, table_td)