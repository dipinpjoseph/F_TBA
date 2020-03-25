function generate_elite_list(commands_list){
    document.getElementById("elite_list").innerHTML  = ""
    for (let each of commands_list){
        document.getElementById("elite_list").innerHTML+= "<div class=\"card\"><div class=\"card-header  bg-dark text-white\">"+
            "Topic: "+each.Topic+"</div><div class=\"card-body\">"+"\""+each.Command+
                " \"</div><div class=\"card-footer  bg-light \">"+"Comment: "+each.Comment+
                    "</div></div><br>"
    }
    sidebar_elite_list()
}
function sidebar_elite_list(){
    document.getElementById("sidebar_list").innerHTML += '<br><h4><a href="The-Elite-List-Home" >The Elite List</a></h4>'+
    '<hr style="background-color:#259fea">'+
    '<ul id="sidebar_list" class="list-group">'+
    '<li><a href="SQL-Commands-List">SQL</a></li>'+
    '<li><a href="Frequent-Linux-Commands-List">Linux</a></li>'+
    '<li><a href="python-tips-and-tricks">Python</a></li>'+
    '</ul>'
     
}
