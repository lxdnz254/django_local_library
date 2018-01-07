from django.test import TestCase

# Create your tests here

from catalog.models import Author, Book

class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'first name')

    def test_date_of_death_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label,'died')

    def test_first_name_max_length(self):
        author=Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length,100)

    def test_object_name_is_last_name_comma_first_name(self):
        author=Author.objects.get(id=1)
        expected_object_name = '%s, %s' % (author.last_name, author.first_name)
        self.assertEquals(expected_object_name,str(author))

    def test_get_absolute_url(self):
        author=Author.objects.get(id=1)
        #This will also fail if the urlconf is not defined.
        self.assertEquals(author.get_absolute_url(),'/catalog/author/1')

class BookModelTest(TestCase):
	
	@classmethod
	def setUpTestData(cls):
		Author.objects.create(first_name='Big', last_name='Bob')
		Book.objects.create(title="Bible", author=Author.objects.get(id=1), summary="The word", isbn="000-0-0000000")
		
	def test_title_label(self):
		book=Book.objects.get(id=1)
		field_label = book._meta.get_field('title').verbose_name
		self.assertEquals(field_label, 'title')
	
	def test_book_author_label(self):
		book=Book.objects.get(id=1)
		field_label = book._meta.get_field('author').verbose_name
		self.assertEquals(field_label, 'author')
		
	def test_title_max_length(self):
		book=Book.objects.get(id=1)
		max_length = book._meta.get_field('title').max_length
		self.assertEquals(max_length, 200)
		
	def test_summary_text(self):
		book=Book.objects.get(id=1)
		field_text = book._meta.get_field('summary').verbose_name
		self.assertEquals(field_text, 'summary')
	
	def test_summary_max_length(self):
		book=Book.objects.get(id=1)
		max_length = book._meta.get_field('summary').max_length
		self.assertEquals(max_length, 1000)
		
	def test_isbn_label(self):
		book = Book.objects.get(id=1)
		isbn = book._meta.get_field('isbn').verbose_name
		self.assertEquals(isbn, 'ISBN')
		
	def test_isbn_max_length(self):
		book = Book.objects.get(id=1)
		max_length = book._meta.get_field('isbn').max_length
		self.assertEquals(max_length, 13)
