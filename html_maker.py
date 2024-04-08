def make_col3(photos):
    cols_3 = ''
    for photo in photos:
        cols_3 += f'''
                    <div class="col-3">
                        <div class="card" style= 'padding: 3rem; background-color:cyan; margin-bottom:2rem; margin-left:2rem; margin-right:3rem' >
                            <img src="{photo['url']}" style='margin-bottom: 3rem' alt=""/>
                            <h4 style='color: red'>{photo['title']}</4>
                        </div>
                    </div>       
        '''
    return cols_3

def crear_html(cols_3):
    cuerpo_html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Título de la Página</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    </head>
    <body class= 'bg-warning'>
        <h1 class='text-center' style= 'padding-top: 2rem; padding-bottom:2rem; color:blue'>Blog Simple</h1>
            <div>
                <div class = "row">
                    {cols_3}
                </div>
            </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    </body>
    </html>
    '''
    return cuerpo_html