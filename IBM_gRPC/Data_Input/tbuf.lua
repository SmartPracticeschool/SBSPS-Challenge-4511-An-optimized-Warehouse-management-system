function put_data(rec, Item_no, Store_no, Transactions, Oil_prices, Holiday, Offer)
  local targeted_cards_pb = require "IBM_pb"
  -- Serialize Example
  local msg = IBM_pb.Request()
  msg.Item_no = Item_no
  msg.Store_no = Store_no
  msg.Transactions = Transactions
  msg.Oil_prices = Oil_prices
  msg.Holiday = Holiday
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
