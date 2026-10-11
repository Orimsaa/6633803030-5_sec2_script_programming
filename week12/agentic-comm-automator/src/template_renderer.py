# agentic-comm-automator/src/template_renderer.py
import string

from utils import setup_logging

logger = setup_logging(__name__)


class TemplateRenderer:
    """
    เติมค่าใน template แบบ f-string ("{report_date}", "{sales_figure:,.2f}") จาก context ของ agent
    """

    def render(self, template_string, context):
        if template_string is None:
            return ""
        try:
            return string.Formatter().vformat(template_string, (), context)
        except KeyError as e:
            logger.error(f"Missing key {e} in template context. Template: '{template_string}'")
            raise ValueError(f"Missing context key: {e}")
