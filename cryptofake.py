from bitcoinlib.wallets import Wallet

# Set up sender and recipient wallet addresses
sender_wallet = Wallet('sender_private_key')
recipient_wallet = 'recipient_public_key'

# Set up transaction details
fee = 0.0001  # transaction fee
amount = 0.1  # amount to send
change = 0.0  # amount to send back to sender
data = None  # transaction data
message = "This is a test transaction"  # transaction message

# Create transaction and sign with sender's private key
tx = sender_wallet.send_to(recipient_wallet, amount, fee, change, data, message)
tx.sign(sender_wallet)

# Broadcast transaction to Bitcoin network
tx.broadcast()
