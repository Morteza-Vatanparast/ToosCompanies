from tornado.web import UIModule


class AdminSidebar(UIModule):
    def render(self):
        return self.render_string('../ui_modules/template/admin/sidebars.html')

    def embedded_javascript(self):
        return u'''
            var link = $("[href='%s']");
            link.addClass('active');
            link.closest('.menu-main-item').addClass('active')
        ''' % self.handler.request.path
