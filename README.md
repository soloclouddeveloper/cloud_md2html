
## cloud_md2html

Converts markdown files to HTML when uploaded to a bucket in GCP.

Python package, Markdown, is used to create the HTML code.  The cloud event, md2html, 
reads in the markdown file, converts to HTML, and then concatenates the common header
and footer HTML code to the converted HTML code, which is then saved in the OUTPUT_BUCKET.

Both MARKDOWN_UPLOAD_BUCKET and OUTPUT_BUCKET are non-public buckets.


'''
gcloud functions deploy md2html \
--gen2 \
--runtime=python312 \
--region=[REGION] \
--source=. \
--entry-point=md2html \
--trigger-event-filters="type=google.cloud.storage.object.v1.finalized" \
--trigger-event-filters="bucket=[MARKDOWN-UPLOAD-BUCKET]" \
--max-instances=5 \
--set-env-vars="TARGET_BUCKET=[HTML-NON-PUBLIC-BUCKET]"
'''

## Header and Footer files

`header.html` and `footer.html` are saved in the OUT_BUCKET


## CSS files

The CSS files are saved in a public bucket.
https://storage.googleapis.com/scd-static-e7w4/css/scd_styles.css

### Image files

https://storage.googleapis.com/scd-static-e7w4/img/<FILENAME>
