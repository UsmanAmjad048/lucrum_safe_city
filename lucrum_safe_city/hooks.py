from . import __version__ as app_version

app_name = "lucrum_safe_city"
app_title = "Lucrum Safe City"
app_publisher = "usman"
app_description = "Lucrum Safe City"
app_email = "usman.amjad@tylextech.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/lucrum_safe_city/css/lucrum_safe_city.css"
# app_include_js = "/assets/lucrum_safe_city/js/lucrum_safe_city.js"

# include js, css files in header of web template
# web_include_css = "/assets/lucrum_safe_city/css/lucrum_safe_city.css"
# web_include_js = "/assets/lucrum_safe_city/js/lucrum_safe_city.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "lucrum_safe_city/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "lucrum_safe_city.utils.jinja_methods",
#	"filters": "lucrum_safe_city.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "lucrum_safe_city.install.before_install"
# after_install = "lucrum_safe_city.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "lucrum_safe_city.uninstall.before_uninstall"
# after_uninstall = "lucrum_safe_city.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See ducky.core.notifications.get_notification_config

# notification_config = "lucrum_safe_city.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "ducky.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "ducky.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"lucrum_safe_city.tasks.all"
#	],
#	"daily": [
#		"lucrum_safe_city.tasks.daily"
#	],
#	"hourly": [
#		"lucrum_safe_city.tasks.hourly"
#	],
#	"weekly": [
#		"lucrum_safe_city.tasks.weekly"
#	],
#	"monthly": [
#		"lucrum_safe_city.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "lucrum_safe_city.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"ducky.desk.doctype.event.event.get_events": "lucrum_safe_city.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Ducky apps
# override_doctype_dashboards = {
#	"Task": "lucrum_safe_city.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["lucrum_safe_city.utils.before_request"]
# after_request = ["lucrum_safe_city.utils.after_request"]

# Job Events
# ----------
# before_job = ["lucrum_safe_city.utils.before_job"]
# after_job = ["lucrum_safe_city.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"lucrum_safe_city.auth.validate"
# ]
