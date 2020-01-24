from django.test import TestCase
from .models import Post,Comment
from django.contrib.auth.models import User

# Create your tests here.
class PostModelsTestCase(TestCase):
    def setUp(self):
        user_1 = User.objects.create_user(
            username="user_1",
            email="user@gmail.com"
        )
        post_1 = Post.objects.create(
            author=user_1,
            postTitle="Post_1 Title",
            postContent="Post_1 Content"
        )
        post_2 = Post.objects.create(
            author=user_1,
            postTitle="Post_2 Title",
            postContent="Post_2 Content"
        )
        comment_1 = Comment.objects.create(
            commenter=user_1,
            post=post_1,
            commentContent="Comment Content by user_1 in post_1"
        )

    def test_postedBy(self):
        user_1 = User.objects.get(pk=1)
        post1 = Post.objects.get(pk=1)
        self.assertEqual(post1.postedBy(), user_1)
        
    def test_commentFrom(self):
        comment = Comment.objects.get(pk=1)
        post1 = Post.objects.get(pk=1)
        post2 = Post.objects.get(pk=2)
        self.assertEqual(comment.commentFrom(),post1)
        self.assertNotEqual(comment.commentFrom(),post2)
