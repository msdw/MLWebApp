from flask import render_template, jsonify, request
from flask.ext.login import current_user
from app.models import User
from app import app, models
from app.toolbox import email
import random
import stripe


stripe.api_key = 'pk_test_6DkaDw0woAqDklauqEUb5rrH00503hwbWm'
secret = 'sk_test_NMsq4qsgfmSTFmEOWNftQTds00zbSF5TSn'
webhook_secret = 'whsec_yFMTEi8c36tEIRXcm8XOjMHDvR93fBhe'


@app.route('/')
@app.route('/index')
def index():
  user = None
  if current_user.is_authenticated:
    user = models.User.query.filter_by(email=current_user.email).first()
  return render_template('index.html', title='Home', user=user)


@app.route('/uploaded', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['file']
		# model = get model here
		img = image.load_img(f.filename)
		preds = model.predict(img)
		return render_template('uploaded.html', predictions=preds_decoded)

@app.route('/map')
def map():
    return render_template('map.html', title='Map')


@app.route('/map/refresh', methods=['POST'])
def map_refresh():
    points = [(random.uniform(48.8434100, 48.8634100),
               random.uniform(2.3388000, 2.3588000))
              for _ in range(random.randint(2, 9))]
    return jsonify({'points': points})


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')


def handle_checkout_session(session, curr_user):
  print('sessionthingy', session)
  print(current_user.is_authenticated)
  print(current_user.is_anonymous)
  user = models.User.query.filter_by(email=curr_user.email).first()
  user.paid = 1
  print("blah")
  db.session.commit()


@app.route("/webhooks", methods=["POST"])
def webhooks():
    print("enter webhook")
    payload = request.data.decode("utf-8")
    received_sig = request.headers.get("Stripe-Signature", None)

    try:
        event = stripe.Webhook.construct_event(
            payload, received_sig, webhook_secret
        )
    except ValueError:
        print("Error while decoding event!")
        return "Bad payload", 400
    except stripe.error.SignatureVerificationError:
        print("Invalid signature!")
        return "Bad signature", 400

    print(
        "Received event: id={id}, type={type}".format(
            id=event.id, type=event.type
        )
    )
    if event['type'] == 'checkout.session.completed':
      session = event['data']['object']

      # Fulfill the purchase...
      handle_checkout_session(session, current_user)

    return "", 200



