{% extends 'templates/default.php' %}

{% block title %}Admin example{% endblock %}

{% block content %}
	<h2>Downloadable files</h2>

	{% if files is empty %}
		<p>No Registed user.</p>
	{% else %}
		{% for file in files %}
			<div>
				
				{% if file != '.'  and file != '..' %}
					<form action="{{ urlFor('example.post') }}" method="post">
						<label for="filename">{{ file }}</label>
						<input type="hidden" name="file1" value="{{ file }}">
						<input type="submit" value="Download">
					</form>

				{% endif %}
			</div>
		{% endfor %}
	{% endif %}
{% endblock %}