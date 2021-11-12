while :
	pass   <ul>
            {% for date in date_list %}
            <li style="list-style:none; display:inline-block">
                <a href="{% url 'blog:post_day_archive' date|date:'Y' month|date:'m' date|date:'d' %}">{{ date|date:'d' }}</a>
            </li>
            {% endfor %}
        </ul>

        <ul>
            {% for post in object_list %}
                <li>{{post.modify_date|date:"Y-m-d"}}&nbsp;&nbsp;&nbsp;
                    <a href="{{post.get_absolute_url}}"><string>{{post.title}}</string></a>
                </li>
            {% endfor %}
        </ul>