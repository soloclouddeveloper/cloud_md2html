#
# ref: https://github.com/GoogleCloudPlatform/functions-framework-python
#
# To Run:
# functions-framework --target md2html --debug
#

import os
import markdown
import functions_framework
from google.cloud import storage
from cloudevents.http.event import CloudEvent

@functions_framework.cloud_event
def md2html(cloud_event: CloudEvent) -> None:
    """Converts a markdown file to HTML.  Triggered when 
    file is created/uploaded to cloud storage bucket.

    The HTML file is then saved to TARGET_BUCKET specified in 
    the environment variable.

    Args:
    cloud_event : The CloudEvent that triggered the function

    Returns:
    None
    """

    target_bucket = os.environ["TARGET_BUCKET"]

    # read all the necessary files in
    data = cloud_event.data

    # if the file isn't markdown (.md), then we are done
    filename_parts = data["name"].split(".")
    num_parts = len(filename_parts)
    if num_parts < 2 or filename_parts[num_parts - 1].lower() != "md":
        return
    
    nav_bar = ''
    if data["name"] == "til/index.md":
        nav_bar = read_bucket_blob_as_text("nav_til_index.html", target_bucket)
    elif data["name"] == "index.md":
        nav_bar = read_bucket_blob_as_text("nav_main_index.html", target_bucket)
    else:
        nav_bar = read_bucket_blob_as_text("nav_til_article.html", target_bucket)

    md_file = read_bucket_blob_as_text(data["name"], data["bucket"])
    html_header = read_bucket_blob_as_text("header.html", target_bucket)
    html_footer = read_bucket_blob_as_text("footer.html", target_bucket)

    # convert markdown to html and assemble final html file
    md_html = markdown.markdown(md_file)
    html_final = html_header + nav_bar + md_html + html_footer

    # change the extension and save to TARGET_BUCKET
    storage_client = storage.Client()
    bucket = storage_client.bucket(target_bucket)
    blob = bucket.blob(data["name"].replace(".md", ".html"))
    blob.upload_from_string(html_final, content_type="text/html")

    delete_markdown_file(data["name"], data["bucket"])


def read_bucket_blob_as_text(blob_name, bucket_name):
    ret_val = ''
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(blob_name)
    ret_val = blob.download_as_text()

    return ret_val

def delete_markdown_file(filename, md_bucket):
    """
    Deletes a file from the bucket

    Args:
        filename: string - name of the folder/file to delete
        md_bucket: string - name of the bucket which contains 
            the file to be deleted.

    Returns:
        None
    """
    storage_client = storage.Client()
    bucket = storage_client.bucket(md_bucket)
    blob = bucket.blob(filename)
    blob.delete()