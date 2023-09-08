---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if site.author.googlescholar %}
  For my most up-to-date research papers, see <u><a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

<h2>Peer-reviewed</h2>
{% for post in site.publications reversed %}
  {% if post.pubtype == 'article' %}
      {% include archive-single.html %}
  {% endif %}
{% endfor %}

<h2>Submitted</h2>
{% for post in site.publications reversed %}
  {% if post.pubtype == 'submitted' %}
      {% include archive-single.html %}
  {% endif %}
{% endfor %}
