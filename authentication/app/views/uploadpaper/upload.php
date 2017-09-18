{% extends 'templates/default.php' %}

{% block title %}Upload paper here{% endblock %}

{% block content %}
	
	<form action="{{ urlFor('upload.post') }}" method="POST" enctype="multipart/form-data" name="FileUploadForm" id="FileUploadForm">


        <label for="UploadFileField"></label>
        <input type="file" name="UploadFileField" id="UploadFileField">
        <input type="submit" name="UploadButton" id="UploadButton" value="Upload">

	
</form>

{% endblock %}