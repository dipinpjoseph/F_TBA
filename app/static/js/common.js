function generate_template(){
    loadHead('<meta charset="utf-8">')
    loadHead('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
	loadHead('<meta name="author" content="Dipin P Joseph">')
    loadHead('<link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">')
    loadHead('<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Charm:700">')
    loadHead('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">')
    loadHead('<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>')
    loadHead('<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>')
    loadHead('<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>')
    loadHead('<link rel="icon" href="../img/logo.png">')
    loadHead('<style>body {font-family: "Times New Roman", Times, serif;}</style>')
    document.getElementById("header_tag").innerHTML = '<header><div class="container-fluid"><h3 style="font-family: \'charm\', serif; "><small><a href="https://www.thebearsenal.com">TheBeArsenal</a></small></h3><hr style="background-color:#259fea"></div></header>'+
    '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>'+
    '<!-- TheBeArsenal_Apps_Head --><ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-3600373850128255" data-ad-slot="7156171146" data-ad-format="auto" data-full-width-responsive="true"></ins><script> (adsbygoogle = window.adsbygoogle || []).push({});</script>'
    document.getElementById("sidebar_list").innerHTML = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>'+
    '<!-- TheBeARsenal_Apps_Vertical_Above_Sidebar -->'+
    '<ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-3600373850128255" data-ad-slot="1355666669" data-ad-format="auto" data-full-width-responsive="true"></ins>'+
    '<script>(adsbygoogle = window.adsbygoogle || []).push({});</script>'+
    '<h4><a href="https://www.thebearsenal.com/apps/home" >Apps</a></h4>'+
    '<hr style="background-color:#259fea"><ul id="sidebar_list" class="list-group">'+
    '<li><a href="https://www.thebearsenal.com/apps/The-Elite-List-Home">The Elite List - Tech Handbook</a></li>'+
    '<li><a href="https://www.thebearsenal.com/apps/NZ-PostCode-Finder">NZ Post Code Finder</a></li>'+
    '<li><a href="https://www.thebearsenal.com/apps/QR-Code-Generator">QR Code Generator</a></li>'+
    '<li><a href="https://www.thebearsenal.com/apps/Bar-Code-Generator">Bar Code Generator</a></li>'+
    '<li><a href="https://www.thebearsenal.com/apps/Find-Permutation-and-Combination-Online">Permutation & Combination</a></li>'+
    '<li><a href="https://www.thebearsenal.com/apps/Morse-Code-Generator">Morse Code Generator</a></li>'+
    '<li><a href="https://www.thebearsenal.com/apps/Online-BMI-Calculator">BMI Calculator</a></li>'+
    '<li><a href="https://www.thebearsenal.com/apps/Extract-Emails-From-Text.html">Email Extractor</a></li></ul>'
    document.getElementById("social_plugins").innerHTML = '<div class="col-2"><a href="https://github.com/dipinpjoseph" target="_blank"><i class="fa fa-github" style="font-size:40px;"></i></a></div>'+
    '<div class="col-2"><a href="https://www.linkedin.com/in/dipinpjoseph/" target="_blank"><i class="fa fa-linkedin-square" style="font-size:40px;"></i></a></div>'+
    '<div class="col-2"><a href="https://twitter.com/thebearsenal" target="_blank"><i class="fa fa-twitter" style="font-size:40px;"></i></a></div>'+
    '<div class="col-2"><a href="https://www.instagram.com/thebearsenal/" target="_blank"><i class="fa fa-instagram" style="font-size:40px;"></i></a></div>'+
    '<div class="col-2"><a href="https://www.facebook.com/TheBeArsenal/" target="_blank"><i class="fa fa-facebook-square" style="font-size:40px;"></i></a></div>'+
    '<div class="col-2"><a href="https://www.youtube.com/channel/UCvfjHPhi9Db_tFZKIbje2zw/" target="_blank"><i class="fa fa-youtube-square" style="font-size:40px;"></i></a></div>'
    document.getElementById("page_footer").innerHTML = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>'+
    '<!-- TheBeArsenal_Apps_Hori_Above_Footer -->'+
    '<ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-3600373850128255" data-ad-slot="3376708233" data-ad-format="auto" data-full-width-responsive="true"></ins>'+
    '<script>(adsbygoogle = window.adsbygoogle || []).push({});</script>'+
    '<div class="footer-copyright text-center py-3" style="font-family: \'Times New Roman\', Times, serif;">&copy; 2020 Copyright:<a href="https://www.thebearsenal.com" style="font-family: \'Times New Roman\', Times, serif;"> The Beginner&apos;s Arsenal</a></div>'
    loadHead('<script data-ad-client="ca-pub-3600373850128255" async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>')
    loadHead('<script async src="https://www.googletagmanager.com/gtag/js?id=UA-33383432-3"></script>')
    //load_ads()
}
function loadHead(data)
{    
    document.getElementsByTagName('head')[0].innerHTML += data
}
function load_ads()
{    
	window.dataLayer = window.dataLayer || [];
		function gtag(){dataLayer.push(arguments);}
		gtag('js', new Date());
		gtag('config', 'UA-33383432-3');
}
