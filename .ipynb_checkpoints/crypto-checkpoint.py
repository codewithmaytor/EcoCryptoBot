{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "dde6f32e-bed2-4939-a792-5e9245cd8ac7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "EcoCryptoBot 🤖🌱: Hello there! I'm EcoCryptoBot, your sustainable crypto advisor.\n",
      "Ask me about trending coins, sustainability, or long-term investment advice!\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  Which crypto should I buy for long-term growth?\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "EcoCryptoBot: 📊 For long-term growth, consider Cardano. It's rising and sustainable!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  Which coins are trending?\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "EcoCryptoBot: These cryptos are trending up: Bitcoin, Solana, Qubic, NATIX Network, Sui, Keeta, Ethereum, Hyperliquid, USD1, Railgun, Fartcoin, Zebec Network, Sophon, Build On BNB, Plume 🚀\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  whats the disclaimer in trading biitcoins\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "EcoCryptoBot: ⚠️ Crypto is risky—always do your own research!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  thankyou\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "EcoCryptoBot: Hmm, I didn't quite catch that. Try asking about trends, sustainability, or prices.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  quit\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "EcoCryptoBot: 👋 Goodbye and good luck with your crypto journey!\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "print(\"EcoCryptoBot 🤖🌱: Hello there! I'm EcoCryptoBot, your sustainable crypto advisor.\")\n",
    "print(\"Ask me about trending coins, sustainability, or long-term investment advice!\\n\")\n",
    "\n",
    "sustainability_scores = {\n",
    "    \"bitcoin\": {\"energy_use\": \"high\", \"score\": 3},\n",
    "    \"ethereum\": {\"energy_use\": \"medium\", \"score\": 6},\n",
    "    \"cardano\": {\"energy_use\": \"low\", \"score\": 8}\n",
    "}\n",
    "\n",
    "\n",
    "def get_trending_coins():\n",
    "    url = \"https://api.coingecko.com/api/v3/search/trending\"\n",
    "    response = requests.get(url)\n",
    "    data = response.json()\n",
    "    trending = [coin['item']['name'] for coin in data['coins']]\n",
    "    return trending\n",
    "\n",
    "\n",
    "def get_price(coin_id):\n",
    "    url = f\"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd\"\n",
    "    response = requests.get(url)\n",
    "    return response.json().get(coin_id, {}).get(\"usd\", \"Price not found\")\n",
    "\n",
    "\n",
    "def recommend_sustainable():\n",
    "    best = max(sustainability_scores.items(), key=lambda x: x[1][\"score\"])\n",
    "    return best[0].capitalize()\n",
    "\n",
    "\n",
    "while True:\n",
    "    user_input = input(\"You: \").lower()\n",
    "\n",
    "    if \"trending\" in user_input or \"rising\" in user_input:\n",
    "        trending = get_trending_coins()\n",
    "        print(f\"EcoCryptoBot: These cryptos are trending up: {', '.join(trending)} 🚀\")\n",
    "\n",
    "    elif \"sustainable\" in user_input:\n",
    "        coin = recommend_sustainable()\n",
    "        print(f\"EcoCryptoBot: 🌱 {coin} is the most sustainable choice with a strong future outlook!\")\n",
    "\n",
    "    elif \"price\" in user_input:\n",
    "        if \"bitcoin\" in user_input:\n",
    "            price = get_price(\"bitcoin\")\n",
    "            print(f\"EcoCryptoBot: 📈 Bitcoin is trading at ${price} USD.\")\n",
    "        elif \"ethereum\" in user_input:\n",
    "            price = get_price(\"ethereum\")\n",
    "            print(f\"EcoCryptoBot: 📈 Ethereum is trading at ${price} USD.\")\n",
    "        elif \"cardano\" in user_input:\n",
    "            price = get_price(\"cardano\")\n",
    "            print(f\"EcoCryptoBot: 📈 Cardano is trading at ${price} USD.\")\n",
    "        else:\n",
    "            print(\"EcoCryptoBot: 🔍 Try asking for the price of Bitcoin, Ethereum, or Cardano.\")\n",
    "\n",
    "    elif \"growth\" in user_input or \"invest\" in user_input or \"long-term\" in user_input:\n",
    "        sustainable = recommend_sustainable()\n",
    "        print(f\"EcoCryptoBot: 📊 For long-term growth, consider {sustainable}. It's rising and sustainable!\")\n",
    "\n",
    "    elif \"disclaimer\" in user_input:\n",
    "        print(\"EcoCryptoBot: ⚠️ Crypto is risky—always do your own research!\")\n",
    "\n",
    "    elif user_input in [\"exit\", \"quit\", \"bye\"]:\n",
    "        print(\"EcoCryptoBot: 👋 Goodbye and good luck with your crypto journey!\")\n",
    "        break\n",
    "\n",
    "    else:\n",
    "        print(\"EcoCryptoBot: Hmm, I didn't quite catch that. Try asking about trends, sustainability, or prices.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b7374dca-e2cd-4dd7-9a82-561a95094ad0",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (2118439407.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  Cell \u001b[0;32mIn[2], line 1\u001b[0;36m\u001b[0m\n\u001b[0;31m    git init\u001b[0m\n\u001b[0m        ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "git init\n",
    "git remote add origin https://github.com/codewithmaytor/EcoCryptoBot.git\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "20a147c0-0902-46b6-a4e3-f414771763e8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
