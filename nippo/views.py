from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import (ListView 
                                  ,DetailView 
                                  ,FormView
                                 )
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import NippoModel
from .forms  import NippoFormClass, NippoModelForm
from django.urls import reverse, reverse_lazy,path
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .filters import  NippoModelFilter
from accounts.models import Profile


# forms.py からフォーム定義をimport
from .forms import ContactForm

# submitイベントの挙動を定義
class ContactFormView(FormView):
    # 表示させる html を指定
    template_name = 'nippo/お問い合わせ.html'
    # form.py で定義したクラス名を指定
    form_class = ContactForm
    # 遷移後のurlを引数で指定
    success_url = reverse_lazy('contact_result')

    # メールを送信
    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
    
def ContactResultView(request): #クラス作成
    return render(request,"nippo/contact_result.html")    
    
def Nippo0000View(request): #クラス作成
    return render(request,"nippo/www.ikedatohka.co.jp.html")

def Nippo0100View(request): #クラス作成
    return render(request,"nippo/製品のご案内｜池田糖化工業株式会社.html")
def Nippo0101View(request): #クラス作成
    return render(request,"nippo/QOL納豆菌 _ 池田糖化工業株式会社.html")
def Nippo0102View(request): #クラス作成
    return render(request,"nippo/ミネラクト乳酸菌 _ 池田糖化工業株式会社.html")
def Nippo0103View(request): #クラス作成
    return render(request,"nippo/ジンジャーエキスＮＥ _ 池田糖化工業株式会社.html")
def Nippo0104View(request): #クラス作成
    return render(request,"nippo/ジンジャーエキスパウダーシリーズ _ 池田糖化工業株式会社.html")
def Nippo0110View(request): #クラス作成
    return render(request,"nippo/プラントdeリッチ｜池田糖化工業株式会社.html")
def Nippo0111View(request): #クラス作成
    return render(request,"nippo/クックミートプラス®｜プラントdeリッチ｜池田糖化工業株式会社.html")
def Nippo0112View(request): #クラス作成
    return render(request,"nippo/クリームテイスト｜プラントdeリッチ｜池田糖化工業株式会社.html")
def Nippo0113View(request): #クラス作成
    return render(request,"nippo/マスキングテイスト®｜プラントdeリッチ｜池田糖化工業株式会社.html")
def Nippo0114View(request): #クラス作成
    return render(request,"nippo/» サンプル請求.html")

def Nippo0120View(request): #クラス作成
    return render(request,"nippo/おすすめ製品｜池田糖化工業株式会社.html")
def Nippo0130View(request): #クラス作成
    return render(request,"nippo/» 製品分類 » 液体・調味.html")
def Nippo013001View(request): #クラス作成
    return render(request,"nippo/中華系調味料 _ 池田糖化工業株式会社.html")
def Nippo013002View(request): #クラス作成
    return render(request,"nippo/醤油ペースト _ 池田糖化工業株式会社.html")
def Nippo013003View(request): #クラス作成
    return render(request,"nippo/その他の液体調味料（焙焼系調味料） _ 池田糖化工業株式会社.html")
def Nippo013004View(request): #クラス作成
    return render(request,"nippo/水産エキス・だし _ 池田糖化工業株式会社.html")
def Nippo013005View(request): #クラス作成
    return render(request,"nippo/畜産エキス _ 池田糖化工業株式会社.html")
def Nippo013006View(request): #クラス作成
    return render(request,"nippo/野菜エキス _ 池田糖化工業株式会社.html")
def Nippo013007View(request): #クラス作成
    return render(request,"nippo/冷凍野菜ペースト _ 池田糖化工業株式会社.html")
def Nippo013008View(request): #クラス作成
    return render(request,"nippo/冷凍オニオンソテー _ 池田糖化工業株式会社.html")
def Nippo013009View(request): #クラス作成
    return render(request,"nippo/国産にんにく _ 池田糖化工業株式会社.html")
def Nippo013010View(request): #クラス作成
    return render(request,"nippo/形のある野菜加工品 _ 池田糖化工業株式会社.html")
def Nippo013011View(request): #クラス作成
    return render(request,"nippo/フライド野菜（乾燥） _ 池田糖化工業株式会社.html")
def Nippo013012View(request): #クラス作成
    return render(request,"nippo/乾燥野菜 _ 池田糖化工業株式会社.html")
def Nippo013013View(request): #クラス作成
    return render(request,"nippo/粉末醤油 _ 池田糖化工業株式会社.html")
def Nippo013014View(request): #クラス作成
    return render(request,"nippo/中華醤パウダー _ 池田糖化工業株式会社.html")
def Nippo013015View(request): #クラス作成
    return render(request,"nippo/野菜（エキス）パウダー _ 池田糖化工業株式会社.html")
def Nippo013016View(request): #クラス作成
    return render(request,"nippo/水産エキスパウダー _ 池田糖化工業株式会社.html")
def Nippo013017View(request): #クラス作成
    return render(request,"nippo/畜肉エキスパウダー _ 池田糖化工業株式会社.html")
def Nippo013018View(request): #クラス作成
    return render(request,"nippo/素材アップパウダー _ 池田糖化工業株式会社.html")
def Nippo0140View(request): #クラス作成
    return render(request,"nippo/» 製品分類 » 顆粒・固形.html")
def Nippo01401View(request): #クラス作成
    return render(request,"nippo/キャラメリゼ _ 池田糖化工業株式会社.html")
def Nippo01402View(request): #クラス作成
    return render(request,"nippo/フルーツ顆粒 _ 池田糖化工業株式会社.html")
def Nippo01403View(request): #クラス作成
    return render(request,"nippo/フルーツチップ _ 池田糖化工業株式会社.html")
def Nippo01404View(request): #クラス作成
    return render(request,"nippo/フルーツパウダー _ 池田糖化工業株式会社.html")
def Nippo01405View(request): #クラス作成
    return render(request,"nippo/キャラメルパウダー _ 池田糖化工業株式会社.html")
def Nippo01406View(request): #クラス作成
    return render(request,"nippo/フルーツソース _ 池田糖化工業株式会社.html")
def Nippo01407View(request): #クラス作成
    return render(request,"nippo/チョコソース _ 池田糖化工業株式会社.html")
def Nippo01408View(request): #クラス作成
    return render(request,"nippo/その他ソース・ペースト・フィリング _ 池田糖化工業株式会社.html")
def Nippo01409View(request): #クラス作成
    return render(request,"nippo/キャラメルソース _ 池田糖化工業株式会社.html")
def Nippo01410View(request): #クラス作成
    return render(request,"nippo/カラメルソース _ 池田糖化工業株式会社.html")
def Nippo0150View(request): #クラス作成
    return render(request,"nippo/» 製品分類 » カラメル色素・天然系色素.html")
def Nippo0160View(request): #クラス作成
    return render(request,"nippo/» 製品分類 » 機能性素材.html")
def Nippo0170View(request): #クラス作成
    return render(request,"nippo/» 製品分類 » 植物エキス.html")
def Nippo0180View(request): #クラス作成
    return render(request,"nippo/酵素｜製品のご案内｜池田糖化工業株式会社.html")


def Nippo0200View(request): #クラス作成
    return render(request,"nippo/中食・外食向け製品.html")
def Nippo0210View(request): #クラス作成
    return render(request,"nippo/オーダーメイドシステム｜中食・外食向け製品｜池田糖化工業株式会社.html")
def Nippo0220View(request): #クラス作成
    return render(request,"nippo/多様な包装形態・流通温度帯｜中食・外食向け製品｜池田糖化工業株式会社.html")
def Nippo0230View(request): #クラス作成
    return render(request,"nippo/ごはん：主食メニュー｜中食・外食向け製品｜池田糖化工業株式会社.html")
def Nippo0231View(request): #クラス作成
    return render(request,"nippo/パスタ：主食メニュー｜中食・外食向け製品｜池田糖化工業株式会社.html")
def Nippo0240View(request): #クラス作成
    return render(request,"nippo/ステーキ・ハンバーグ：メインメニュー｜中食・外食向け製品｜池田糖化工業株式会社.html")
def Nippo0241View(request): #クラス作成
    return render(request,"nippo/オーブン料理：メインメニュー｜中食・外食向け製品｜池田糖化工業株式会社.html")
def Nippo0242View(request): #クラス作成
    return render(request,"nippo/中華料理：メインメニュー｜中食・外食向け製品｜池田糖化工業株式会社.html")
def Nippo0243View(request): #クラス作成
    return render(request,"nippo/揚げ物：メインメニュー｜中食・外食向け製品｜池田糖化工業株式会社.html")
def Nippo0244View(request): #クラス作成
    return render(request,"nippo/焼き物：メインメニュー｜中食・外食向け製品｜池田糖化工業株式会社.html")
def Nippo0245View(request): #クラス作成
    return render(request,"nippo/煮込みのタレ：メインメニュー｜中食・外食向け製品｜池田糖化工業株式会社.html")
def Nippo0250View(request): #クラス作成
    return render(request,"nippo/スープ：サイドメニュー｜中食・外食向け製品｜池田糖化工業株式会社.html")
def Nippo0260View(request): #クラス作成
    return render(request,"nippo/パン：スイーツメニュー｜中食・外食向け製品｜池田糖化工業株式会社.html")
def Nippo0261View(request): #クラス作成
    return render(request,"nippo/ケーキ：スイーツメニュー｜中食・外食向け製品｜池田糖化工業株式会社.html")
def Nippo0262View(request): #クラス作成
    return render(request,"nippo/ドリンク：スイーツメニュー｜中食・外食向け製品｜池田糖化工業株式会社.html")
def Nippo0263View(request): #クラス作成
    return render(request,"nippo/アイスクリーム：スイーツメニュー｜中食・外食向け製品｜池田糖化工業株式会社.html")
def Nippo0264View(request): #クラス作成
    return render(request,"nippo/パフェ：スイーツメニュー｜中食・外食向け製品｜池田糖化工業株式会社.html")


def Nippo0300View(request): #クラス作成
    return render(request,"nippo/微生物 受託培養.html")

def Nippo0400View(request): #クラス作成
    return render(request,"nippo/企業情報.html")
def Nippo0410View(request): #クラス作成
    return render(request,"nippo/トップメッセージ｜企業情報｜池田糖化工業株式会社.html")
def Nippo0420View(request): #クラス作成
    return render(request,"nippo/①食とのつながり｜企業情報｜池田糖化工業株式会社.html")
def Nippo0430View(request): #クラス作成
    return render(request,"nippo/②食とのつながり｜企業情報｜池田糖化工業株式会社.html")
def Nippo0440View(request): #クラス作成
    return render(request,"nippo/③食とのつながり｜企業情報｜池田糖化工業株式会社.html")
def Nippo0450View(request): #クラス作成
    return render(request,"nippo/④食とのつながり｜企業情報｜池田糖化工業株式会社.html")
def Nippo0460View(request): #クラス作成
    return render(request,"nippo/会社概要｜企業情報｜池田糖化工業株式会社.html")
def Nippo0470View(request): #クラス作成
    return render(request,"nippo/池田糖化の歴史｜企業情報｜池田糖化工業株式会社.html")
def Nippo0480View(request): #クラス作成
    return render(request,"nippo/事業拠点｜企業情報｜池田糖化工業株式会社.html")

def Nippo0500View(request): #クラス作成
    return render(request,"nippo/製造技術・設備.html")
def Nippo0510View(request): #クラス作成
    return render(request,"nippo/乾燥粉末化｜製造技術・設備｜池田糖化工業株式会社.html")
def Nippo0520View(request): #クラス作成
    return render(request,"nippo/造粒｜製造技術・設備｜池田糖化工業株式会社.html")
def Nippo0530View(request): #クラス作成
    return render(request,"nippo/粉体ブレンド｜製造技術・設備｜池田糖化工業株式会社.html")
def Nippo0540View(request): #クラス作成
    return render(request,"nippo/アセプティック｜製造技術・設備｜池田糖化工業株式会社.html")
def Nippo0550View(request): #クラス作成
    return render(request,"nippo/レトルト｜製造技術・設備｜池田糖化工業株式会社.html")
def Nippo0560View(request): #クラス作成
    return render(request,"nippo/液体ブレンド｜製造技術・設備｜池田糖化工業株式会社.html")
def Nippo0570View(request): #クラス作成
    return render(request,"nippo/フリーズドライ｜製造技術・設備｜池田糖化工業株式会社.html")
def Nippo0580View(request): #クラス作成
    return render(request,"nippo/小袋包装｜製造技術・設備｜池田糖化工業株式会社.html")
def Nippo0590View(request): #クラス作成
    return render(request,"nippo/バイオ関係設備｜製造技術・設備｜池田糖化工業株式会社.html")

def Nippo0600View(request): #クラス作成
    return render(request,"nippo/食の安全と安心.html")
def Nippo0610View(request): #クラス作成
    return render(request,"nippo/食の安全・品質方針｜食の安全と安心｜池田糖化工業株式会社.html")
def Nippo0620View(request): #クラス作成
    return render(request,"nippo/原材料の管理｜食の安全と安心｜池田糖化工業株式会社.html")
def Nippo0630View(request): #クラス作成
    return render(request,"nippo/フードディフェンス体制：生産工場での取り組み｜食の安全と安心｜池田糖化工業株式会社.html")
def Nippo0640View(request): #クラス作成
    return render(request,"nippo/異物混入防止対策：生産工場での取り組み｜食の安全と安心｜池田糖化工業株式会社.html")
def Nippo0650View(request): #クラス作成
    return render(request,"nippo/製造工程管理：生産工場での取り組み｜食の安全と安心｜池田糖化工業株式会社.html")

def Nippo0700View(request): #クラス作成
    return render(request,"nippo/研究開発.html")
def Nippo0710View(request): #クラス作成
    return render(request,"nippo/研究領域・体制：研究開発の概要｜研究開発｜池田糖化工業株式会社.html")
def Nippo0711View(request): #クラス作成
    return render(request,"nippo/拠点紹介：研究開発の概要｜研究開発｜池田糖化工業株式会社.html")
def Nippo0712View(request): #クラス作成
    return render(request,"nippo/開発から製品になるまで：研究開発の概要｜研究開発｜池田糖化工業株式会社.html")
def Nippo0720View(request): #クラス作成
    return render(request,"nippo/美味しさ：私たちの目指すもの｜研究開発｜池田糖化工業株式会社.html")
def Nippo0721View(request): #クラス作成
    return render(request,"nippo/彩り：私たちの目指すもの｜研究開発｜池田糖化工業株式会社.html")
def Nippo0722View(request): #クラス作成
    return render(request,"nippo/ヘルスケア：私たちの目指すもの｜研究開発｜池田糖化工業株式会社.html")
def Nippo0730View(request): #クラス作成
    return render(request,"nippo/玉井 秀樹：研究開発の声｜研究開発｜池田糖化工業株式会社.html")
def Nippo0731View(request): #クラス作成
    return render(request,"nippo/藤丸 美南海：研究開発の声｜研究開発｜池田糖化工業株式会社.html")
def Nippo0732View(request): #クラス作成
    return render(request,"nippo/松本 絵里加：研究開発の声｜研究開発｜池田糖化工業株式会社.html")
def Nippo0733View(request): #クラス作成
    return render(request,"nippo/三島 彩夏：研究開発の声｜研究開発｜池田糖化工業株式会社.html")
def Nippo0734View(request): #クラス作成
    return render(request,"nippo/赤木 孝成：研究開発の声｜研究開発｜池田糖化工業株式会社.html")
def Nippo0735View(request): #クラス作成
    return render(request,"nippo/平山 大剛：研究開発の声｜研究開発｜池田糖化工業株式会社.html")
def Nippo0740View(request): #クラス作成
    return render(request,"nippo/論文発表｜研究開発｜池田糖化工業株式会社.html")

def Nippo0800View(request): #クラス作成
    return render(request,"nippo/採用情報.html")
def Nippo0810View(request): #クラス作成
    return render(request,"nippo/新卒社員募集要項｜採用情報｜池田糖化工業株式会社.html")
def Nippo0820View(request): #クラス作成
    return render(request,"nippo/求める人物像｜採用情報｜池田糖化工業株式会社.html")
def Nippo0830View(request): #クラス作成
    return render(request,"nippo/選考プロセス｜採用情報｜池田糖化工業株式会社.html")
def Nippo0840View(request): #クラス作成
    return render(request,"nippo/説明会・選考会スケジュール｜採用情報｜池田糖化工業株式会社.html")
def Nippo0850View(request): #クラス作成
    return render(request,"nippo/Q&A｜採用情報｜池田糖化工業株式会社.html")
def Nippo0860View(request): #クラス作成
    return render(request,"nippo/仕事内容｜採用情報｜池田糖化工業株式会社.html")
def Nippo0870View(request): #クラス作成
    return render(request,"nippo/キャリア採用募集要項｜採用情報｜池田糖化工業株式会社.html")

#def Nippo0900View(request): #クラス作成
#    return render(request,"nippo/お問い合わせ.html")




def Nippo1000View(request): #クラス作成
    return render(request,"nippo/サイトマップ.html")

def Nippo1100View(request): #クラス作成
    return render(request,"nippo/プライバシーポリシー.html")




def Nippo1300View(request): #クラス作成
    return render(request,"nippo/ニュースリリース.html")
def Nippo1301View(request): #クラス作成
    return render(request,"nippo/2023-1.html")
def Nippo1302View(request): #クラス作成
    return render(request,"nippo/2023-2.html")