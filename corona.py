import csv

def createSite():
    with open("site.html", "w") as file:
        htmlCode = """
       <html>
        <head>
         <meta charset="utf-8">
         <!-- Chargement de la librairie Javascript à utiliser -->
         <!-- depuis Internet 
         <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.bundle.min.js"></script> -->
         
         <!-- Localement -->
         <script src="package\dist\Chart.bundle.min.js"></script>
         
         <title>Nombre de nouveaux cas en Italie</title>
        </head>
        <body>
          <canvas id="graphique" width="50px" height="50px"></canvas>
          <script>
        // l'identifiant est celui du canevas
        var ctx = document.getElementById('graphique').getContext('2d');
        // création du graphique
        var myChart = new Chart(ctx, {{
        type: 'bar',   // le type du graphique
        data: {{        // les données
            labels: {},
            datasets: [{{
                        label: 'new cases',
                        data: {}
                       }}]
               }}
             }}
        );
          </script>

        </body>
       </html>""".format(csvWork()[0], csvWork()[1])
        file.write(htmlCode)
        
def csvWork():
    Dates = []
    NCases = []
    with open('full_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["location"] == "Italy":
                if row["new_cases"] == "":
                    NCases.append("0")
                else:
                    Dates.append(row["date"])
                    NCases.append(row["new_cases"])
            if row["location"] == "Jamaica":
                break
    return [Dates, NCases]
