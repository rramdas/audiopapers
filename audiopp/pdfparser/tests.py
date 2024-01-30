from django.test import TestCase
from django.urls import resolve, reverse


class PaperListViewTest(TestCase):

    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_name(self):
        response = self.client.get(reverse('paper_list'))
        self.assertEqual(response.status_code, 200)
    
    def test_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'paper_list.html') 
        

# class PaperTestCase(TestCase):

#     def setUp(self):
#         self.paper = UploadedPaper.objects.create(title="test", authors="test", abstract="test") 


#     # test uploading the pdf file
#     def test_upload_file(self):
#         """Upload a pdf file."""
#         # create a file to upload
#         file = SimpleUploadedFile("test.pdf", b"file_content", content_type="pdf")
#         # upload the file
#         response = self.client.post("/upload/", {"pdf": file})
#         # check that the file was uploaded
#         self.assertEqual(response.status_code, 302)
#         # check that the file was parsed
#         self.assertEqual(Paper.objects.count(), 1)
#         # check that the file was parsed correctly
#         paper = Paper.objects.get(title="test")
#         self.assertEqual(paper.title, "test")
#         self.assertEqual(paper.authors, "test")
#         self.assertEqual(paper.abstract, "test")
    
