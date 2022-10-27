"""Main module."""
from dataclasses import dataclass
import pytesseract
from PIL import Image
from pathlib import Path
import re

from typing import Optional, List


_REGEX = r'(?P<area>[\d,\.\s]+)(?:(?:sq|square)[\. ]*(?:ft|feet)|sqft)'


def extract_number(s: str) -> float:
	digits = re.sub(r'[^0-9\.]', "", s)
	try:
		return float(digits)
	except ValueError:
		return None


@dataclass
class ParseResult:
	raw_string: str

	@property
	def matches(self) -> List[str]:
		return re.findall(_REGEX, self.raw_string, re.IGNORECASE)

	@property
	def numbers(self) -> List[Optional[float]]:
		return list(map(extract_number, self.matches))

	@property
	def area(self) -> Optional[float]:
		if len(self.numbers) > 0:
			return max(self.numbers)
		else:
			None


class PlanParser:
	def parse(image_file: Path) -> ParseResult:
		image = Image.open(image_file)
		return ParseResult(pytesseract.image_to_string(image))