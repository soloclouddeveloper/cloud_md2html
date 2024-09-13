
### Markdown to HTML Conversion using Cloud Run Function

For years I've tried to keep a blog using free Wordpress or Blogger sites.  I do
good for a while but then give up.  One thing that I never did like was the
UI to write the blog.  It always seemed that eventually I would want to tweak something
in an article and it was just a PITA to do using the tools.

As I moved to self-hosting I tried creating my own blogging UI only to run into the same
problems.  I then [Derek Sivers](sive.rs) wrote an article of how he writes his articles in
plain text then goes backs and wraps everything in HTML paragraph tags.  I started using 
this method and liked it much better.

Then, I started using markdown more for work and found out that this gave me the right
amount of control I was looking for.  I would still need to tweak here and there but
for the most part this works best for me.

Needing a project to use Cloud Functions (now Cloud Run Functions) and Eventarcs, created
a small python script that builds a blog page for me.  I write the main body in markdown,
upload to a private storage bucket in GCP which fires off the function.  The function
converts the markdown and slaps a header and footer around the body of the text.

Still a bit clunky and I've been tweaking it lately.  But for me, this is the best 
solution thus far.

Below is an architectual diagram of the project.

![cloud run function architectual diagram](https://storage.googleapis.com/scd-static-e7w4/img/md2html.drawio.svg)

**Date posted: 2024-09-10**