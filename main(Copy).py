const { Client, GatewayIntentBits } = require('discord.js');
const client = new Client({ intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent] });

const token = 'MTI1ODcxMDI4NDQxMTg2MzA3MA.GOYm-F.EvKMx-pTs3FgVT3QrAaJ_HMJrtpBLA80KEl7G0';

client.once('ready', () => {
    console.log('Bot is online!');
});

client.on('messageCreate', message => {
    if (message.content === '!ping') {
        message.channel.send('Pong!');
    }
});

client.login(token);
