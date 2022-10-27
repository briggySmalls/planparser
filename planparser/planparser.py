"""Main module."""
from dataclasses import dataclass
import pytesseract
from PIL import Image
from pathlib import Path


@dataclass
class ParseResult:
	raw_string: str

	def area(self) -> float:
		return 0


class PlanParser:
	def parse(image_file: Path) -> ParseResult:
		image = Image.open(image_file)
		return ParseResult(pytesseract.image_to_string(image))