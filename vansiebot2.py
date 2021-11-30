import sys
from telethon import TelegramClient
import time
import datetime
starttime = time.time()

api_id = 17585481
api_hash = '9bb5ba7a249bc35854639c2ce3f44573'

groups = ['bscgemhunters', 'bscbunnys', 'bscstreetbetscaptain', 'wolvesofbscstreet', 'bscgemarmy', 'thedefiapechat', 'gemsfordegensgroup', 'bscape', 'chatbsc', 'bscsimpers', 'defiexperts', 'rugorriches', 'bscdegens', 'kingoffomo', 'binancechainlovers', 'bscbscdefiexperts', 'earlybscfarm', 'bscmoonz', 'spacegem', 'smartchainapes', 'chatbsc', 'bscgemarmy', 'unitedshillers', 'bitsquad', 'satoshiclub', 'cryptofamilygroup', 'elliotradescrypto', 'tradecoinunderground', 'cryptodakurobinhooders', 'moonhunters', 'tehmoonwalksrs', 'defiracoons', 'uniswapgemsv2', 'defi', 'gemcollectors', 'dexgemschat', 'uniswapresearch', 'infinitygainzz', 'uniswaplegit', 'acmecrypto', 'oddgemsfamilia', 'thegemhunterstg', 'uniswapgemspumpz', 'whalersclub101', 'uniswapchina', 'cryptosupportservices', 'uniswapgem123', 'uniswapearlycalls', 'cryptoevolution1', 'overdosegemsgroup', 'gemsnipers', 'infinitygainzz', 'unigemchatz', 'supergemhunter', 'thetradingpit', 'deficrew', 'farmingroom', 'pumpchads', 'uniswapone', 'shitcoinzcz', 'uniswapgemalerts', 'binancedextrading', 'uniswapunofficial', 'cryptopricetalks', 'gemsfordegensgroup', 'gemdiscussion', 'gemtalkc', 'infinitybotz', 'cryptomindsgroup', 'themoonboyschat', 'sgdefi', 'uniswapgemgroup', 'uniswapgemdiscuss', 'defisearch', 'suicidalpumpgroup', 'illuminatigem',]

failcount = 0;

while true:
    with TelegramClient('anon', api_id, api_hash) as client:
        for x in groups:
            try:
                client.loop.run_untill_complete(client.send_message(x, 'hi'))
            except:
                print(x, sys.exc_info()[0])
                failcount += 1
    print(datetime.datetime.now(), str(Failcount/len(groups) *100)) + '%'
    Time.sleep(10800 - ((Time.Time() - StartTime) % 10800))