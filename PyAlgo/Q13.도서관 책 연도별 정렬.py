def solution(data):
  book, years = data
  return sorted(book, key=lambda book: (years[book], book))