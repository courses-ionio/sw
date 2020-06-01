exports.handler = function(context, event, callback) {
  # lista apo tous arithmous pou vriskontai stin mavri lista, xorismenoi apo koma.
  # stin diki mou periptwsi einai mono o enas arithmos pou moy dothike apo to free trial tou twilio

  let blacklist = event.blacklist || [ "+12057406383" ];  
  let twiml = new Twilio.twiml.VoiceResponse();
  let blocked = true;
  if (blacklist.length > 0) {
    if (blacklist.indexOf(event.From) === -1) {
      blocked = false;
    }
  }
  if (blocked) {
    twiml.reject();
  }
  else {
  # an o arithmos den anhkei stous mplokarismenous tote exw dhmioyrghsei, mesw tou twilio bin na phgainei ena hxitiko mhnuma
  twiml.redirect("https://handler.twilio.com/twiml/EHad2b74da4da9760127864786227706cd");
  }
  callback(null, twiml);
};
