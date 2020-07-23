function put_data(rec, Transactions, Oil_Prices, Holiday, Offer)
  local IBM_pb = require "IBM_pb"
  -- Serialize Example
  local msg = IBM_pb.Request()
  msg.Transactions = Transactions
  msg.Oil_Prices = Oil_Prices
  msg.Holiday = Holiday
  msg.Offer = Offer
  local pb_data = msg:SerializeToString()
  local pb_bytes = bytes(pb_data:len())
  bytes.set_type(pb_bytes, 4)
  bytes.set_string(pb_bytes, 1, pb_data)
  rec["store_details"] = pb_bytes
  if aerospike:exists(rec) then
    aerospike:update(rec)
  else
    aerospike:create(rec)
  end
end
