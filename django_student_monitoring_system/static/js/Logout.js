function logout() {
    var home = "{% url 'Logout' %}";
    window.location.href = home;
  }