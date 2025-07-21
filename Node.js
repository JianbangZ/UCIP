const protobuf = require('protobufjs');
protobuf.load('ucip.proto', (err, root) => {
  if (err) throw err;
  const UCIP = root.lookupType('UCIP');
  
  const payload = { version: '1.0', userId: 'user-123', timestamp: '2025-07-21T12:00:00Z', consent: { granted: true, scopes: ['basic'] } };
  const errMsg = UCIP.verify(payload);
  if (errMsg) throw Error(errMsg);
  
  const message = UCIP.create(payload);
  const buffer = UCIP.encode(message).finish();
  const decoded = UCIP.decode(buffer);
  console.log(decoded);
});
