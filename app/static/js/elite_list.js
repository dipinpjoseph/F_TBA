function generate_elite_list(commands_list){
    document.getElementById("elite_list").innerHTML  = ""
    for (let each of commands_list){
        document.getElementById("elite_list").innerHTML+= "<div class=\"card\"><div class=\"card-header  bg-primary text-white\">"+
            "Topic: "+each.Topic+"</div><div class=\"card-body\">"+"\""+each.Command+
                " \"</div><div class=\"card-footer  bg-dark text-white\">"+"Comment: "+each.Comment+
                    "</div></div><br>"
    }
    sidebar_elite_list()
}
function sidebar_elite_list(){
    document.getElementById("sidebar_list").innerHTML += '<br><h4><a href="https://www.thebearsenal.com/apps/The-Elite-List-Home" >The Elite List</a></h4>'+
    '<hr style="background-color:#259fea">'+
    '<ul id="sidebar_list" class="list-group">'+
    '<li><a href="https://www.thebearsenal.com/apps/SQL-Commands-List">SQL Commands</a></li>'+
    '<li><a href="https://www.thebearsenal.com/apps/Frequent-Linux-Commands-List">Linux Hacks</a></li>'+
    '<li><a href="https://www.thebearsenal.com/apps/python-tips-and-tricks">Python Short Notes</a></li>'+
    '</ul>'
     
}