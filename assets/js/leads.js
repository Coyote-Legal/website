(function () {
  var FALLBACK_EMAIL = 'baba@coyotelegal.com';

  function endpointReady() {
    return typeof LEADS_ENDPOINT === 'string' && LEADS_ENDPOINT.indexOf('http') === 0;
  }

  function mailtoFallback(payload) {
    var subject = encodeURIComponent('Coyote Legal Lead — ' + (payload.name || 'Website'));
    var lines = [];
    Object.keys(payload).forEach(function (key) {
      if (payload[key]) lines.push(key + ': ' + payload[key]);
    });
    window.location.href =
      'mailto:' + FALLBACK_EMAIL + '?subject=' + subject + '&body=' + encodeURIComponent(lines.join('\n'));
  }

  window.coyoteSubmitLead = function (payload, onDone) {
    payload.timestamp = new Date().toISOString();
    payload.page = window.location.pathname;

    if (!endpointReady()) {
      console.warn('Coyote Legal: LEADS_ENDPOINT not configured — using mailto fallback.');
      mailtoFallback(payload);
      if (onDone) onDone(false);
      return;
    }

    fetch(LEADS_ENDPOINT, {
      method: 'POST',
      mode: 'no-cors',
      headers: { 'Content-Type': 'text/plain;charset=utf-8' },
      body: JSON.stringify(payload)
    })
      .then(function () {
        if (onDone) onDone(true);
      })
      .catch(function () {
        mailtoFallback(payload);
        if (onDone) onDone(false);
      });
  };
})();
