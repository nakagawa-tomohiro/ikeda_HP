from django.urls import path,include
from .views import (
             
                    Nippo0000View,
                    Nippo0100View,
                    Nippo0101View,
                    Nippo0102View,
                    Nippo0103View,
                    Nippo0104View,
                    Nippo0110View,
                    Nippo0111View,
                    Nippo0112View,
                    Nippo0113View,
                    Nippo0114View,
                    Nippo0120View,
                    Nippo0130View,
                    Nippo013001View,
                    Nippo013002View,
                    Nippo013003View,
                    Nippo013004View,
                    Nippo013005View,
                    Nippo013006View,
                    Nippo013007View,
                    Nippo013008View,
                    Nippo013009View,
                    Nippo013010View,
                    Nippo013011View,
                    Nippo013012View,
                    Nippo013013View,
                    Nippo013014View,
                    Nippo013015View,
                    Nippo013016View,
                    Nippo013017View,
                    Nippo013018View,
                    Nippo0140View,
                    Nippo01401View,
                    Nippo01402View,
                    Nippo01403View,
                    Nippo01404View,
                    Nippo01405View,
                    Nippo01406View,
                    Nippo01407View,
                    Nippo01408View,
                    Nippo01409View,
                    Nippo01410View,
                    Nippo0150View,
                    Nippo0160View,
                    Nippo0170View,
                    Nippo0180View,
                    Nippo0200View,                
                    Nippo0210View,
                    Nippo0220View,
                    Nippo0230View,
                    Nippo0231View,
                    Nippo0240View,
                    Nippo0241View,
                    Nippo0242View,
                    Nippo0243View,
                    Nippo0244View,
                    Nippo0245View,
                    Nippo0250View,
                    Nippo0260View,
                    Nippo0261View,
                    Nippo0262View,
                    Nippo0263View,
                    Nippo0264View,
                    Nippo0300View,
                    Nippo0400View,
                    Nippo0410View,
                    Nippo0420View,
                    Nippo0430View,
                    Nippo0440View,
                    Nippo0450View,
                    Nippo0460View,
                    Nippo0470View,
                    Nippo0480View,
                    Nippo0500View,
                    Nippo0500View,
                    Nippo0510View,
                    Nippo0520View,
                    Nippo0530View,
                    Nippo0540View,
                    Nippo0550View,
                    Nippo0560View,
                    Nippo0570View,
                    Nippo0580View,
                    Nippo0590View,
                    Nippo0600View,
                    Nippo0610View,
                    Nippo0620View,
                    Nippo0630View,
                    Nippo0640View,
                    Nippo0650View,
                    Nippo0700View,
                    Nippo0710View, 
                    Nippo0711View, 
                    Nippo0712View, 
                    Nippo0720View, 
                    Nippo0721View, 
                    Nippo0722View, 
                    Nippo0730View, 
                    Nippo0731View, 
                    Nippo0732View,
                    Nippo0733View,
                    Nippo0734View,
                    Nippo0735View, 
                    Nippo0740View,
                    Nippo0800View,
                    Nippo0810View,
                    Nippo0820View,
                    Nippo0830View,
                    Nippo0840View,
                    Nippo0850View,
                    Nippo0860View,
                    Nippo0870View,
                    ContactFormView,
                    ContactResultView,
                    Nippo1000View,
                    Nippo1100View,
       
                    Nippo1300View,
                    Nippo1301View,
                    Nippo1302View,
                  )

urlpatterns = [
  
  path("www.ikedatohka.co.jp/"                                              ,Nippo0000View, name="www.ikedatohka.co.jp"),
  path("製品のご案内｜池田糖化工業株式会社/"                                 ,Nippo0100View, name="製品のご案内｜池田糖化工業株式会社"),
  path("QOL納豆菌 _ 池田糖化工業株式会社/"                                   ,Nippo0101View, name="QOL納豆菌 _ 池田糖化工業株式会社"),
  path("ミネラクト乳酸菌 _ 池田糖化工業株式会社/"                            ,Nippo0102View, name="ミネラクト乳酸菌 _ 池田糖化工業株式会社"),
  path("ジンジャーエキスＮＥ _ 池田糖化工業株式会社/"                        ,Nippo0103View, name="ジンジャーエキスＮＥ _ 池田糖化工業株式会社"),
  path("ジンジャーエキスパウダーシリーズ _ 池田糖化工業株式会社/"            ,Nippo0104View, name="ジンジャーエキスパウダーシリーズ _ 池田糖化工業株式会社"),
  path("プラントdeリッチ｜池田糖化工業株式会社/"                             ,Nippo0110View, name="プラントdeリッチ｜池田糖化工業株式会社"),
  path("クックミートプラス®｜プラントdeリッチ｜池田糖化工業株式会社/"        ,Nippo0111View, name="クックミートプラス®｜プラントdeリッチ｜池田糖化工業株式会社"),
  path("クリームテイスト｜プラントdeリッチ｜池田糖化工業株式会社/"           ,Nippo0112View, name="クリームテイスト｜プラントdeリッチ｜池田糖化工業株式会社"),
  path("マスキングテイスト®｜プラントdeリッチ｜池田糖化工業株式会社/"        ,Nippo0113View, name="マスキングテイスト®｜プラントdeリッチ｜池田糖化工業株式会社"),
  path("» サンプル請求/"                                                    ,Nippo0114View, name="» サンプル請求"),
  path("おすすめ製品｜池田糖化工業株式会社/"                                 ,Nippo0120View, name="おすすめ製品｜池田糖化工業株式会社"),
  path("» 製品分類 » 液体・調味/"                                            ,Nippo0130View, name="» 製品分類 » 液体・調味"),
  path("中華系調味料 _ 池田糖化工業株式会社/"                                ,Nippo013001View, name="中華系調味料 _ 池田糖化工業株式会社"),
  path("醤油ペースト _ 池田糖化工業株式会社/"                                ,Nippo013002View, name="醤油ペースト _ 池田糖化工業株式会社"),
  path("その他の液体調味料（焙焼系調味料） _ 池田糖化工業株式会社/"           ,Nippo013003View, name="その他の液体調味料（焙焼系調味料） _ 池田糖化工業株式会社"),
  path("水産エキス・だし _ 池田糖化工業株式会社/"                            ,Nippo013004View, name="水産エキス・だし _ 池田糖化工業株式会社"),
  path("畜産エキス _ 池田糖化工業株式会社/"                                  ,Nippo013005View, name="畜産エキス _ 池田糖化工業株式会社"),
  path("野菜エキス _ 池田糖化工業株式会社/"                                  ,Nippo013006View, name="野菜エキス _ 池田糖化工業株式会社"),
  path("冷凍野菜ペースト _ 池田糖化工業株式会社/"                            ,Nippo013007View, name="冷凍野菜ペースト _ 池田糖化工業株式会社"),
  path("冷凍オニオンソテー _ 池田糖化工業株式会社/"                          ,Nippo013008View, name="冷凍オニオンソテー _ 池田糖化工業株式会社"),
  path("国産にんにく _ 池田糖化工業株式会社/"                                ,Nippo013009View, name="国産にんにく _ 池田糖化工業株式会社"),
  path("形のある野菜加工品 _ 池田糖化工業株式会社/"                           ,Nippo013010View, name="形のある野菜加工品 _ 池田糖化工業株式会社"),
  path("フライド野菜（乾燥） _ 池田糖化工業株式会社/"                         ,Nippo013011View, name="フライド野菜（乾燥） _ 池田糖化工業株式会社"),
  path("乾燥野菜 _ 池田糖化工業株式会社/"                                     ,Nippo013012View, name="乾燥野菜 _ 池田糖化工業株式会社"),
  path("粉末醤油 _ 池田糖化工業株式会社/"                                     ,Nippo013013View, name="粉末醤油 _ 池田糖化工業株式会社"),
  path("中華醤パウダー _ 池田糖化工業株式会社/"                               ,Nippo013014View, name="中華醤パウダー _ 池田糖化工業株式会社"),
  path("野菜（エキス）パウダー _ 池田糖化工業株式会社/"                        ,Nippo013015View, name="野菜（エキス）パウダー _ 池田糖化工業株式会社"),
  path("水産エキスパウダー _ 池田糖化工業株式会社/"                            ,Nippo013016View, name="水産エキスパウダー _ 池田糖化工業株式会社"),
  path("畜肉エキスパウダー _ 池田糖化工業株式会社/"                            ,Nippo013017View, name="畜肉エキスパウダー _ 池田糖化工業株式会社"),
  path("素材アップパウダー _ 池田糖化工業株式会社/"                            ,Nippo013018View, name="素材アップパウダー _ 池田糖化工業株式会社"),
  path("» 製品分類 » 顆粒・固形/"                                            ,Nippo0140View, name="» 製品分類 » 顆粒・固形"),
  path("キャラメリゼ _ 池田糖化工業株式会社/"                                ,Nippo01401View, name="キャラメリゼ _ 池田糖化工業株式会社"),
  path("フルーツ顆粒 _ 池田糖化工業株式会社/"                                ,Nippo01402View, name="フルーツ顆粒 _ 池田糖化工業株式会社"),
  path("フルーツチップ _ 池田糖化工業株式会社/"           ,Nippo01403View, name="フルーツチップ _ 池田糖化工業株式会社"),
  path("フルーツパウダー _ 池田糖化工業株式会社/"                            ,Nippo01404View, name="フルーツパウダー _ 池田糖化工業株式会社"),
  path("キャラメルパウダー _ 池田糖化工業株式会社/"                                  ,Nippo01405View, name="キャラメルパウダー _ 池田糖化工業株式会社"),
  path("フルーツソース _ 池田糖化工業株式会社/"                                  ,Nippo01406View, name="フルーツソース _ 池田糖化工業株式会社"),
  path("チョコソース _ 池田糖化工業株式会社/"                            ,Nippo01407View, name="チョコソース _ 池田糖化工業株式会社"),
  path("その他ソース・ペースト・フィリング _ 池田糖化工業株式会社/"                          ,Nippo01408View, name="その他ソース・ペースト・フィリング _ 池田糖化工業株式会社"),
  path("キャラメルソース _ 池田糖化工業株式会社/"                                ,Nippo01409View, name="キャラメルソース _ 池田糖化工業株式会社"),
  path("カラメルソース _ 池田糖化工業株式会社/"                           ,Nippo01410View, name="カラメルソース _ 池田糖化工業株式会社"),
  path("» 製品分類 » カラメル色素・天然系色素/"                                            ,Nippo0150View, name="» 製品分類 » カラメル色素・天然系色素"), 
  path("» 製品分類 » 機能性素材/"                                            ,Nippo0160View, name="» 製品分類 » 機能性素材"), 
  path("» 製品分類 » 植物エキス/"                                            ,Nippo0170View, name="» 製品分類 » 植物エキス"), 
  path("酵素｜製品のご案内｜池田糖化工業株式会社/"                                            ,Nippo0180View, name="酵素｜製品のご案内｜池田糖化工業株式会社"), 
  
  
  path("中食・外食向け製品/"                                                 ,Nippo0200View, name="中食・外食向け製品"), 
  path("オーダーメイドシステム｜中食・外食向け製品｜池田糖化工業株式会社/"    ,Nippo0210View, name="オーダーメイドシステム｜中食・外食向け製品｜池田糖化工業株式会社"), 
  path("多様な包装形態・流通温度帯｜中食・外食向け製品｜池田糖化工業株式会社/",Nippo0220View, name="多様な包装形態・流通温度帯｜中食・外食向け製品｜池田糖化工業株式会社"), 
  path("ごはん：主食メニュー｜中食・外食向け製品｜池田糖化工業株式会社/"      ,Nippo0230View, name="ごはん：主食メニュー｜中食・外食向け製品｜池田糖化工業株式会社"), 
  path("パスタ：主食メニュー｜中食・外食向け製品｜池田糖化工業株式会社/"      ,Nippo0231View, name="パスタ：主食メニュー｜中食・外食向け製品｜池田糖化工業株式会社"), 
  path("ステーキ・ハンバーグ：メインメニュー｜中食・外食向け製品｜池田糖化工業株式会社/",Nippo0240View, name="ステーキ・ハンバーグ：メインメニュー｜中食・外食向け製品｜池田糖化工業株式会社"), 
  path("オーブン料理：メインメニュー｜中食・外食向け製品｜池田糖化工業株式会社/",Nippo0241View, name="オーブン料理：メインメニュー｜中食・外食向け製品｜池田糖化工業株式会社"), 
  path("中華料理：メインメニュー｜中食・外食向け製品｜池田糖化工業株式会社/"  ,Nippo0242View, name="中華料理：メインメニュー｜中食・外食向け製品｜池田糖化工業株式会社"), 
  path("揚げ物：メインメニュー｜中食・外食向け製品｜池田糖化工業株式会社/"    ,Nippo0243View, name="揚げ物：メインメニュー｜中食・外食向け製品｜池田糖化工業株式会社"), 
  path("焼き物：メインメニュー｜中食・外食向け製品｜池田糖化工業株式会社/"    ,Nippo0244View, name="焼き物：メインメニュー｜中食・外食向け製品｜池田糖化工業株式会社"), 
  path("煮込みのタレ：メインメニュー｜中食・外食向け製品｜池田糖化工業株式会社/" ,Nippo0245View, name="煮込みのタレ：メインメニュー｜中食・外食向け製品｜池田糖化工業株式会社"), 
  path("スープ：サイドメニュー｜中食・外食向け製品｜池田糖化工業株式会社/"    ,Nippo0250View, name="スープ：サイドメニュー｜中食・外食向け製品｜池田糖化工業株式会社"),
  path("パン：スイーツメニュー｜中食・外食向け製品｜池田糖化工業株式会社/"    ,Nippo0260View, name="パン：スイーツメニュー｜中食・外食向け製品｜池田糖化工業株式会社"),
  path("ケーキ：スイーツメニュー｜中食・外食向け製品｜池田糖化工業株式会社/"  ,Nippo0261View, name="ケーキ：スイーツメニュー｜中食・外食向け製品｜池田糖化工業株式会社"),
  path("ドリンク：スイーツメニュー｜中食・外食向け製品｜池田糖化工業株式会社/", Nippo0262View, name="ドリンク：スイーツメニュー｜中食・外食向け製品｜池田糖化工業株式会社"),
  path("アイスクリーム：スイーツメニュー｜中食・外食向け製品｜池田糖化工業株式会社/" ,Nippo0263View, name="アイスクリーム：スイーツメニュー｜中食・外食向け製品｜池田糖化工業株式会社"),
  path("パフェ：スイーツメニュー｜中食・外食向け製品｜池田糖化工業株式会社/"  ,Nippo0264View, name="パフェ：スイーツメニュー｜中食・外食向け製品｜池田糖化工業株式会社"),
  path("微生物 受託培養/"                                                    ,Nippo0300View, name="微生物 受託培養"),
  path("企業情報/"                                                           ,Nippo0400View, name="企業情報"),
  path("トップメッセージ｜企業情報｜池田糖化工業株式会社/"                    ,Nippo0410View, name="トップメッセージ｜企業情報｜池田糖化工業株式会社"),
  path("①食とのつながり｜企業情報｜池田糖化工業株式会社/"                     ,Nippo0420View, name="①食とのつながり｜企業情報｜池田糖化工業株式会社"),
  path("②食とのつながり｜企業情報｜池田糖化工業株式会社/"                     ,Nippo0430View, name="②食とのつながり｜企業情報｜池田糖化工業株式会社"),
  path("③食とのつながり｜企業情報｜池田糖化工業株式会社/"                     ,Nippo0440View, name="③食とのつながり｜企業情報｜池田糖化工業株式会社"),
  path("④食とのつながり｜企業情報｜池田糖化工業株式会社/"                     ,Nippo0450View, name="④食とのつながり｜企業情報｜池田糖化工業株式会社"),
  path("会社概要｜企業情報｜池田糖化工業株式会社/"                            ,Nippo0460View, name="会社概要｜企業情報｜池田糖化工業株式会社"),
  path("池田糖化の歴史｜企業情報｜池田糖化工業株式会社/"                      ,Nippo0470View, name="池田糖化の歴史｜企業情報｜池田糖化工業株式会社"),
  path("事業拠点｜企業情報｜池田糖化工業株式会社/"                            ,Nippo0480View, name="事業拠点｜企業情報｜池田糖化工業株式会社"),
  path("製造技術・設備/"                                                     ,Nippo0500View, name="製造技術・設備"),
  path("乾燥粉末化｜製造技術・設備｜池田糖化工業株式会社/"                    ,Nippo0510View, name="乾燥粉末化｜製造技術・設備｜池田糖化工業株式会社"),
  path("造粒｜製造技術・設備｜池田糖化工業株式会社/"                          ,Nippo0520View, name="造粒｜製造技術・設備｜池田糖化工業株式会社"),
  path("粉体ブレンド｜製造技術・設備｜池田糖化工業株式会社/"                  ,Nippo0530View, name="粉体ブレンド｜製造技術・設備｜池田糖化工業株式会社"),
  path("アセプティック｜製造技術・設備｜池田糖化工業株式会社/"                ,Nippo0540View, name="アセプティック｜製造技術・設備｜池田糖化工業株式会社"),
  path("レトルト｜製造技術・設備｜池田糖化工業株式会社/"                      ,Nippo0550View, name="レトルト｜製造技術・設備｜池田糖化工業株式会社"),
  path("液体ブレンド｜製造技術・設備｜池田糖化工業株式会社/"                  ,Nippo0560View, name="液体ブレンド｜製造技術・設備｜池田糖化工業株式会社"),
  path("フリーズドライ｜製造技術・設備｜池田糖化工業株式会社/"                ,Nippo0570View, name="フリーズドライ｜製造技術・設備｜池田糖化工業株式会社"),
  path("小袋包装｜製造技術・設備｜池田糖化工業株式会社/"                      ,Nippo0580View, name="小袋包装｜製造技術・設備｜池田糖化工業株式会社"),
  path("バイオ関係設備｜製造技術・設備｜池田糖化工業株式会社/"                ,Nippo0590View, name="バイオ関係設備｜製造技術・設備｜池田糖化工業株式会社"),
  path("食の安全と安心/"                                                     ,Nippo0600View, name="食の安全と安心"),
  path("食の安全・品質方針｜食の安全と安心｜池田糖化工業株式会社/"            ,Nippo0610View, name="食の安全・品質方針｜食の安全と安心｜池田糖化工業株式会社"),
  path("原材料の管理｜食の安全と安心｜池田糖化工業株式会社/"                  ,Nippo0620View, name="原材料の管理｜食の安全と安心｜池田糖化工業株式会社"),
  path("フードディフェンス体制：生産工場での取り組み｜食の安全と安心｜池田糖化工業株式会社/"     ,Nippo0630View, name="フードディフェンス体制：生産工場での取り組み｜食の安全と安心｜池田糖化工業株式会社"),
  path("異物混入防止対策：生産工場での取り組み｜食の安全と安心｜池田糖化工業株式会社/"           ,Nippo0640View, name="異物混入防止対策：生産工場での取り組み｜食の安全と安心｜池田糖化工業株式会社"),
  path("製造工程管理：生産工場での取り組み｜食の安全と安心｜池田糖化工業株式会社/"               ,Nippo0650View, name="製造工程管理：生産工場での取り組み｜食の安全と安心｜池田糖化工業株式会社"),
  path("研究開発/"                                                           ,Nippo0700View, name="研究開発"),
  path("研究領域・体制：研究開発の概要｜研究開発｜池田糖化工業株式会社/"      ,Nippo0710View, name="研究領域・体制：研究開発の概要｜研究開発｜池田糖化工業株式会社"),
  path("拠点紹介：研究開発の概要｜研究開発｜池田糖化工業株式会社/"            ,Nippo0711View, name="拠点紹介：研究開発の概要｜研究開発｜池田糖化工業株式会社"),
  path("開発から製品になるまで：研究開発の概要｜研究開発｜池田糖化工業株式会社/"  ,Nippo0712View, name="開発から製品になるまで：研究開発の概要｜研究開発｜池田糖化工業株式会社"),
  path("美味しさ：私たちの目指すもの｜研究開発｜池田糖化工業株式会社/"        ,Nippo0720View, name="美味しさ：私たちの目指すもの｜研究開発｜池田糖化工業株式会社"),
  path("彩り：私たちの目指すもの｜研究開発｜池田糖化工業株式会社/"            ,Nippo0721View, name="彩り：私たちの目指すもの｜研究開発｜池田糖化工業株式会社"),
  path("ヘルスケア：私たちの目指すもの｜研究開発｜池田糖化工業株式会社/"      ,Nippo0722View, name="ヘルスケア：私たちの目指すもの｜研究開発｜池田糖化工業株式会社"),
  path("玉井 秀樹：研究開発の声｜研究開発｜池田糖化工業株式会社/"             ,Nippo0730View, name="玉井 秀樹：研究開発の声｜研究開発｜池田糖化工業株式会社"),
  path("藤丸 美南海：研究開発の声｜研究開発｜池田糖化工業株式会社/"           ,Nippo0731View, name="藤丸 美南海：研究開発の声｜研究開発｜池田糖化工業株式会社"),
  path("松本 絵里加：研究開発の声｜研究開発｜池田糖化工業株式会社/"           ,Nippo0732View, name="松本 絵里加：研究開発の声｜研究開発｜池田糖化工業株式会社"),
  path("三島 彩夏：研究開発の声｜研究開発｜池田糖化工業株式会社/"             ,Nippo0733View, name="三島 彩夏：研究開発の声｜研究開発｜池田糖化工業株式会社"),
  path("赤木 孝成：研究開発の声｜研究開発｜池田糖化工業株式会社/"             ,Nippo0734View, name="赤木 孝成：研究開発の声｜研究開発｜池田糖化工業株式会社"),
  path("平山 大剛：研究開発の声｜研究開発｜池田糖化工業株式会社/"             ,Nippo0735View, name="平山 大剛：研究開発の声｜研究開発｜池田糖化工業株式会社"),
  path("論文発表｜研究開発｜池田糖化工業株式会社/"                            ,Nippo0740View, name="論文発表｜研究開発｜池田糖化工業株式会社"),
  path("採用情報/"                                                           ,Nippo0800View, name="採用情報"),
  path("新卒社員募集要項｜採用情報｜池田糖化工業株式会社/"                    ,Nippo0810View, name="新卒社員募集要項｜採用情報｜池田糖化工業株式会社"),
  path("求める人物像｜採用情報｜池田糖化工業株式会社/"                        ,Nippo0820View, name="求める人物像｜採用情報｜池田糖化工業株式会社"),
  path("選考プロセス｜採用情報｜池田糖化工業株式会社/"                        ,Nippo0830View, name="選考プロセス｜採用情報｜池田糖化工業株式会社"),
  path("説明会・選考会スケジュール｜採用情報｜池田糖化工業株式会社/"          ,Nippo0840View, name="説明会・選考会スケジュール｜採用情報｜池田糖化工業株式会社"),
  path("Q&A｜採用情報｜池田糖化工業株式会社/"                                 ,Nippo0850View, name="Q&A｜採用情報｜池田糖化工業株式会社"),
  path("仕事内容｜採用情報｜池田糖化工業株式会社/"                            ,Nippo0860View, name="仕事内容｜採用情報｜池田糖化工業株式会社"),
  path("キャリア採用募集要項｜採用情報｜池田糖化工業株式会社/"                ,Nippo0870View, name="キャリア採用募集要項｜採用情報｜池田糖化工業株式会社"),
  path("お問い合わせ/"                                                       ,ContactFormView.as_view(), name="お問い合わせ"),
  path('contract_result/'                                                    ,ContactResultView, name='contact_result'),

  path("サイトマップ/"                                                       ,Nippo1000View, name="サイトマップ"),
  path("プライバシーポリシー/"                                               ,Nippo1100View, name="プライバシーポリシー"),
  path("プライバシーポリシー/"                                               ,Nippo1100View, name="プライバシーポリシー"),
  
  path("ニュースリリース/"                                                   ,Nippo1300View, name="ニュースリリース"),
  path("2023-1/"                                                             ,Nippo1301View, name="2023-1"),
  path("2023-2/"                                                             ,Nippo1302View, name="2023-2"),
]