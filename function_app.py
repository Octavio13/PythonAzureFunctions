import logging
import datetime
import azure.functions as func

app = func.FunctionApp()

@app.schedule(schedule="0 14 * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def octavio_timer_trigger_function(myTimer: func.TimerRequest) -> None:
    
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    
    if myTimer.past_due:
        logging.info('The timer is past due!')

    print('Python timer trigger function ran at %s', utc_timestamp)
    logging.info('Python timer trigger function ran at %s', utc_timestamp)



@app.route(route="octavio_http_trigger_function", auth_level=func.AuthLevel.ANONYMOUS)
def octavio_http_trigger_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )