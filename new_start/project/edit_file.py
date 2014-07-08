#!/usr/bin/env python

class edit_invoice:
    def __init__(self):
        self.fd_temp = open("../Database/invoice/invoice_temp.html", "r+")
        self.fd = open("../Database/invoice/invoice.html", "r+")
    def edit_invoice_number(self, invoice_number):
        self.edit_basic_info("invoice_number", invoice_number)
    def edit_client_tel(self, tel):
        self.edit_basic_info("client_tel", tel)
    def edit_client_addr(self, addr):
        self.edit_basic_info("client_addr", addr)
    def edit_client_name(self, name):
        self.edit_basic_info("client_name", name)
    def edit_car_make(self, car_make):
        self.edit_basic_info("car_make", car_make)
    def edit_car_rego(self, car_rego):
        self.edit_basic_info("car_rego", car_rego)
    def edit_car_odo(self, car_odo):
        self.edit_basic_info("car_odo", car_odo)
    def edit_sub_total(self, sub_total):
        self.edit_basic_info("sub_total", sub_total)
    def edit_gst(self, gst):
        self.edit_basic_info("gst", gst)
    def edit_total(self, total):
        self.edit_basic_info("total_", total)
    def edit_service(self, service):
        self.edit_others("Services", service)
    def edit_labour(self, labour):
        self.edit_others("Labour", labour)
    def edit_notes(self, notes):
        self.edit_others("Notes", notes)
    def edit_others(self, edit_what, info):
        self.fd = open("../Database/invoice/invoice.html", "r+")
        info = "<div class='panel-body'><p>" + info + "</p></div>"
        data = self.fd.read()
        index = data.index(edit_what)
        data = data[0:index + 27] + info +data[index + len(edit_what) + 33:]
        self.fd.seek(0)
        self.fd.truncate()
        self.fd.write(data)
        self.fd.close()
    def edit_basic_info(self, edit_what, info):
        if edit_what == 'invoice_number':
            data = self.fd_temp.read()
            index = data.index(edit_what)
            data = data[0: index] + info + data[index + len(edit_what):]
            self.fd.seek(0)
            self.fd.truncate()
            self.fd.write(data)
            self.fd.close()
        else:
            self.fd = open("../Database/invoice/invoice.html", "r+")
            data = self.fd.read()
            index = data.index(edit_what)
            data = data[0: index] + info + data[index + len(edit_what):]
            self.fd.seek(0)
            self.fd.truncate()
            self.fd.write(data)

if __name__ == "__main__":
    client_name = "Tan"
    invoice_number = "001"
    client_tel = "022 103 8068"
    addr = "Wellington, Nz"
    car_make = "Toyota"
    car_rego = "bla"
    car_odo = "hehe"
    sub_total = "300"
    gst = "100"
    total = "400"
    services = "skdjhfjhfjkhsdkhsdkjfh"
    labour = "skdjhfjhfjkhsdkhsdkjfh"
    notes = "skdjhfjhfjkhsdkhsdkjfh"
    edit = edit_invoice()
    edit.edit_invoice_number(invoice_number)
    edit.edit_client_name(client_name)
    edit.edit_client_tel(client_tel)
    edit.edit_client_addr(addr)
    edit.edit_car_make(car_make)
    edit.edit_car_rego(car_rego)
    edit.edit_car_odo(car_odo)
    edit.edit_sub_total(sub_total)
    edit.edit_gst(gst)
    edit.edit_total(total)
    edit.edit_service(services)
    edit.edit_labour(labour)
    edit.edit_notes(notes)
