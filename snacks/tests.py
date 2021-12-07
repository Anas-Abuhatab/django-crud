from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snack


class SnackTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.Snack = Snack.objects.create(
            title="pickle", description=1, purchaser=self.user,
        )

    def test_string_representation(self):
        self.assertEqual(str(self.Snack), "pickle")

    def test_Snack_content(self):
        self.assertEqual(f"{self.Snack.title}", "pickle")
        self.assertEqual(f"{self.Snack.purchaser}", "tester")
        self.assertEqual(self.Snack.description, 1)

    def test_Snack_list_view(self):
        response = self.client.get(reverse("List_View"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "pickle")
        self.assertTemplateUsed(response, "snack_List.html")

    def test_Snack_detail_view(self):
        response = self.client.get(reverse("Detail_View", args="1"))
        # no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(no_response.status_code, 404)
        # self.assertContains(response, "Purchaser: tester")
        self.assertTemplateUsed(response, "Snack_Detail.html")

    def test_Snack_create_view(self):
        response = self.client.post(
            reverse("Create_View"),
            {
                "title": "Rake",
                "description": "2",
                "purchaser": self.user.id,
            }, follow=True
        )

        self.assertRedirects(response, reverse("Detail_View", args="2"))
        self.assertContains(response, "Details about Rake")

    def test_Snack_update_view_redirect(self):
        response = self.client.post(
            reverse("Update_View", args="1"),
            {"name": "Updated name","rating":"3","reviewer":self.user.id}
        )

        self.assertRedirects(response, reverse("Detail_View", args="1"))

    def test_Snack_delete_view(self):
        response = self.client.get(reverse("Delete_View", args="1"))
        self.assertEqual(response.status_code, 200)