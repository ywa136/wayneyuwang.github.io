---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if site.author.googlescholar %}
  You can also find my articles on <u><a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% for post in site.publications reversed %}
  {% if post.pubtype == 'article' %}
      {% include archive-single.html %}
  {% endif %}
{% endfor %}

<h1>Submitted</h1>
{% for post in site.publications reversed %}
  {% if post.pubtype == 'submitted' %}
      {% include archive-single.html %}
  {% endif %}
{% endfor %}
