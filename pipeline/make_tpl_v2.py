"""Derive infographic_v2_tpl.html from the v1 template (asserted replacements)."""
from paths import ROOT, PIPE, DATA, SITE, DOCS
import os
s = open(f"{PIPE}/infographic_v1_tpl.html").read()

def rep(old, new, count=1):
    global s
    assert s.count(old) >= 1, f"not found: {old[:80]}"
    s = s.replace(old, new, count)

# --- masthead + hero
rep("<title>HN AI Setup Census 2026 — čo ľudia na Hacker News reálne používajú</title>", "<title>AI Setup Census 2026 — čo IT komunita reálne používa (HN · Lobste.rs · Tildes)</title>")
rep("<b>HN AI Setup Census</b> · Ročník 2026", "<b>AI Setup Census</b> · Ročník 2026")
rep("<span>5. 11. 2025 – 5. 11. 2026</span>", "<span>1. 1. – 5. 11. 2026</span>")
rep("<span>Hacker News · Ask HN + osobné blogy</span>", "<span>Hacker News · Lobste.rs · Tildes · blogy</span>")
rep("<h1>Čo HN <em>naozaj</em> používa na prácu s&nbsp;AI</h1>", "<h1>Čo IT komunita <em>naozaj</em> používa na prácu s&nbsp;AI</h1>")
a = s.index('<p class="dek">'); b = s.index("</p>", a) + 4
s = s[:a] + '''<p class="dek">Prečítali sme <strong id="h-com"></strong> komentárov z Hacker News, Lobste.rs a Tildes za rok 2026 a k tomu osobné blogy. Každý autor sa ráta raz na tool a iba vtedy, keď ho <strong>sám aktuálne používa</strong>. Novinka tejto verzie: <strong>cez aké rozhranie</strong> ľudia s AI pracujú a <strong>ako sa líšia komunity</strong>.</p>''' + s[b:]
rep("autorov, ktorí opísali svoj setup, používa <b>Claude Code</b>.", "autorov, ktorí opísali svoj setup, používa <b>Claude Code</b>.")

# --- new sections 02 sources + 03 interfaces after section 01
NEW = '''
  <!-- sources side by side -->
  <section>
    <div class="sh rv"><div class="sec-no">02</div><div>
      <h2>Komunity vedľa seba: rovnaký líder, iný chvost</h2>
      <p class="lede">Podiel autorov v každom zdroji, ktorí tool používajú. Farba bunky zodpovedá podielu v riadku. Blogy = autori článkov o vlastnom setupe (1 hlas na autora). Píšu najmä nadšenci, takže sú prirodzene „pro-AI“.</p>
    </div></div>
    <div class="rv" style="overflow-x:auto"><table class="heat" id="srcmap"></table></div>
    <p class="note rv" id="src-note"></p>
  </section>

  <!-- interfaces -->
  <section>
    <div class="sh rv"><div class="sec-no">03</div><div>
      <h2>Rozhrania: terminál vládne, ale nie sám</h2>
      <p class="lede">Cez aký povrch ľudia s nástrojom alebo modelom pracujú. <b>Plná výplň</b> = autor rozhranie výslovne uviedol. <b>Šrafovanie</b> = doplnené podľa predvoleného rozhrania nástroja (napríklad „Codex CLI“ → terminál), pretože väčšina ľudí ho nespomenie.</p>
    </div></div>
    <div class="grid2">
      <div class="rv"><p class="eyebrow">Typ rozhrania · unikátni autori · <span class="sw" style="background:var(--ink)"></span>výslovne <span class="sw" style="background:repeating-linear-gradient(-45deg,var(--ink) 0 2px,transparent 2px 6px);outline:1px solid var(--ink)"></span>doplnené</p><div class="bars" id="b-iface"></div>
        <p class="eyebrow" style="margin-top:34px">Hostiteľ: v čom to beží (výslovne uvedené)</p><div class="bars" id="b-host"></div></div>
      <div class="rv"><p class="eyebrow">Claude Code: rozhranie tam, kde ho autor uviedol</p><div class="bars" id="b-ccsplit"></div>
        <p class="note" id="cc-note"></p>
        <p class="eyebrow" style="margin-top:34px">GitHub Copilot: rozhranie tam, kde ho autor uviedol</p><div class="bars" id="b-cpsplit"></div></div>
    </div>
    <p class="eyebrow rv" style="margin-top:44px">Model × cez čo ho autor používa · počty autorov, ktorí párovanie výslovne uviedli</p>
    <div class="rv" style="overflow-x:auto"><table class="heat" id="viamap"></table></div>
    <p class="note rv">Claude sa používa prevažne cez <b>Claude Code</b>. Otvorené modely (Qwen, DeepSeek, GLM) idú hlavne cez otvorené harnessy <b>Pi</b> a <b>OpenCode</b>, cez <b>OpenRouter</b> alebo priamo cez <b>llama.cpp</b>. GPT sa najčastejšie páruje s <b>Codex CLI</b>.</p>
  </section>
'''
rep("  <!-- 2 trend -->", NEW + "\n  <!-- 2 trend -->")

# --- surveys section before articles
SURV = '''  <!-- surveys -->
  <section>
    <div class="sh rv"><div class="sec-no">09</div><div>
      <h2>Kalibrácia: komunita vs. veľké ankety 2026</h2>
      <p class="lede">Podiel komunity = autori používajúci tool / <span class="mono" id="n-harn"></span> autorov, ktorí uviedli aspoň jeden coding harness. Ankety sa pýtajú inak („za posledný rok“, „v práci týždenne“, „pravidelní používatelia agentov“), preto porovnávaj <b>poradie a smer</b>, nie absolútne percentá.</p>
    </div></div>
    <div class="rv" id="surveys"></div>
    <div class="legend rv" id="s-leg"></div>
    <p class="note rv">HN, Lobste.rs a Tildes sú oproti priemeru výrazne <b>terminálové a open-source</b>: Pi má v komunite 3× väčší podiel ako v Stack Overflow ankete a OpenCode 2× väčší ako u JetBrains. <b>Copilot, Cursor a JetBrains AI</b> sú naopak výrazne pod priemerom. Tieto nástroje používa najmä „tichá väčšina“ vo firmách, ktorá v takýchto vláknach nepíše.</p>
    <p class="qn rv">Zdroje: <a href="https://survey.stackoverflow.co/2026/ai/data/ai-code-agent">Stack Overflow Developer Survey 2026</a> (n≈12 260, „used in the past year“) · <a href="https://blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/">JetBrains Developer Ecosystem 2026</a> (n&gt;15 000, máj–júl, „at work“) · <a href="https://newsletter.pragmaticengineer.com/p/ai-tooling-2026">Pragmatic Engineer AI Tooling 2026</a> (n=507 pravidelných používateľov agentov).</p>
  </section>

'''
rep("  <!-- 7 articles -->", SURV + "  <!-- 7 articles -->")

# --- renumber
for old, new in [('<div class="sec-no">02</div><div>\n      <h2>Trend', '<div class="sec-no">04</div><div>\n      <h2>Trend'),
                 ('<div class="sec-no">03</div><div>\n      <h2>Modely', '<div class="sec-no">05</div><div>\n      <h2>Modely'),
                 ('<div class="sec-no">04</div><div>\n      <h2>Peniaze', '<div class="sec-no">06</div><div>\n      <h2>Peniaze'),
                 ('<div class="sec-no">05</div><div>\n      <h2>Odchody', '<div class="sec-no">07</div><div>\n      <h2>Odchody'),
                 ('<div class="sec-no">06</div><div>\n      <h2>Lokálne', '<div class="sec-no">08</div><div>\n      <h2>Lokálne'),
                 ('<div class="sec-no">07</div><div>\n      <h2>Ako to', '<div class="sec-no">10</div><div>\n      <h2>Ako to'),
                 ('<div class="sec-no">08</div><div>\n      <h2>Zdroje: 21', '<div class="sec-no">11</div><div>\n      <h2>Zdroje: 21')]:
    rep(old, new)

# --- text updates
rep("Podiel a nie absolútne čísla, pretože veľkosť vzorky kolíše (Q4 2026 tvorí takmer celé jedno veľké vlákno).", "Podiel a nie absolútne čísla, pretože veľkosť vzorky kolíše (Q4 tvorí najmä jedno veľké HN vlákno z novembra).")
rep("<h2>Peniaze: medián $60 mesačne, chvost v tisícoch</h2>", '<h2>Peniaze: medián <span id="h-med"></span> mesačne, chvost v tisícoch</h2>')
rep('<p class="lede">11 článkov o osobnom setupe z HN titulky. Do štatistiky sa započítal iba autor článku, komentáre pod článkom nie.</p>',
    '<p class="lede"><span id="n-art"></span> článkov o osobnom setupe z roku 2026 od <span id="n-auth-b"></span> autorov (HN titulka + knižnica a ITech feedy v Readwise Reader vrátane Swamp Club). Do štatistiky sa započítal iba autor článku, komentáre pod článkom nie. Nižšie je jeden článok na autora, najviac 24.</p>')
rep("<h2>Zdroje: 21 vlákien Ask HN</h2>", "<h2>Zdroje a najbohatšie vlákna</h2>")
rep('<p class="lede">Počet autorov, ktorí vo vlákne opísali vlastný setup, a top 3 harnessy alebo appky v ňom.</p>',
    '<p class="lede">Koľko sme prečítali, koľko autorov opísalo vlastný setup a ktoré vlákna boli najbohatšie (podľa počtu autorov so setupom).</p>')
rep('<table class="threads rv" id="threads"></table>', '<div class="srcgrid rv" id="srcsum"></div>')

# --- methodology
a = s.index('<div class="method rv">'); b = s.index("</section>", a)
s = s[:a] + '''<div class="method rv">
      <div><h4>Postup</h4><ol>
        <li>HN (Algolia API): 21 ručne schválených vlákien Ask HN o setupe a workflow, z toho 19 s komentármi z roku 2026. Lobste.rs (JSON API) a Tildes: 213 diskusií o AI v praxi z roku 2026.</li>
        <li>Stiahnuté celé stromy komentárov, iba komentáre z roku 2026 (<span id="m-com"></span>).</li>
        <li>Každý komentár prečítal LLM, bez predfiltra, a určil tool, stav <i>uses/left</i>, rozhranie, hostiteľa a párovanie model → harness.</li>
        <li>Blogy: HN titulka + Readwise Reader (knižnica later/starred/archive a 100 ITech feedov vrátane Swamp Club). Triedenie podľa názvu a súhrnu, potom LLM čítal plný text. Ráta sa iba autor.</li>
        <li>Normalizácia aliasov, deduplikácia autor × tool, posledný stav vyhráva.</li>
      </ol></div>
      <div><h4>Pravidlá počítania</h4><ul>
        <li>Jednotka = unikátny autor × tool v rámci zdroja. Rovnaká prezývka na dvoch weboch sa ráta ako dvaja autori.</li>
        <li>Ráta sa iba vlastné aktuálne používanie, nie odporúčania ani „počul som“.</li>
        <li>Rozhranie: výslovne uvedené vs. doplnené podľa predvoleného rozhrania nástroja, obe čísla sú zobrazené.</li>
        <li>Ankety sú len kalibrácia a do rebríčkov sa nezlučujú.</li>
        <li>Tools s menej ako 3 autormi nie sú v grafoch (long tail).</li>
      </ul></div>
      <div><h4>Skreslenia a limity</h4><ul>
        <li>Diskusné komunity nie sú reprezentatívna vzorka vývojárov, sú viac terminálové a open-source.</li>
        <li>HN vlákno o lokálnych modeloch (jún) nadhodnocuje Qwen, DeepSeek, Pi a OpenCode.</li>
        <li>Swamp je produkt komunity Swamp Club, preto je v porovnaní zdrojov vynechaný.</li>
        <li><b>Reddit vynechaný:</b> Reddit Responsible Builder Policy vyžaduje schválenie API a výskum mimo programu Reddit for Researchers zakazuje.</li>
        <li>Klasifikácia LLM: 99,6 % citácií overených doslovne proti zdrojovému komentáru.</li>
      </ul></div>
    </div>
  ''' + s[b:]
rep('''<footer><span>Dáta: <a href="mentions.csv">mentions.csv</a> · Report: <a href="report.md">report.md</a> · Spec: <a href="spec.md">spec.md</a></span>''',
    '''<footer><span>Zdroje dát: Hacker News · Lobste.rs · Tildes · osobné blogy · ankety SO / JetBrains / Pragmatic Engineer</span>''')

# --- CSS additions
CSS = '''.heat{border-collapse:collapse;font-family:var(--mono);font-size:12.5px;min-width:100%}
.heat th{font-weight:400;color:var(--ink2);padding:4px 6px;text-align:left;vertical-align:bottom}
.heat thead th span{writing-mode:vertical-rl;transform:rotate(180deg);display:inline-block;max-height:150px;white-space:nowrap;font-family:var(--body);font-size:14px;color:var(--ink)}
.heat tbody th{font-family:var(--body);font-size:16px;color:var(--ink);white-space:nowrap;padding-right:16px}
.heat tbody th small{display:block;font-family:var(--mono);font-size:10.5px;color:var(--mute)}
.heat td{width:56px;height:42px;text-align:center;border:2px solid var(--paper);background:color-mix(in srgb, var(--hn) calc(var(--a) * 100%), var(--paper2));color:var(--ink);font-weight:600}
.heat td.hi{color:#fff}
.heat td.z{color:var(--mute);font-weight:400}
.srcgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border-top:1px solid var(--ink)}
.srcgrid > div{padding:20px 22px 22px 0;border-right:1px solid var(--rule);padding-left:22px}
.srcgrid > div:first-child{padding-left:0}
.srcgrid > div:last-child{border-right:0}
.srcgrid h3{font-family:var(--display);font-size:26px;margin:0 0 6px}
.srcgrid .k{font-family:var(--mono);font-size:12px;color:var(--ink2);margin-bottom:14px}
.srcgrid ol{padding-left:20px;margin:0;font-size:14.5px}
.srcgrid li{margin-bottom:7px}
.srcgrid li small{font-family:var(--mono);color:var(--mute);font-size:11px;margin-left:4px}
.sv{display:grid;grid-template-columns:150px 1fr;align-items:center;gap:14px;padding:9px 0;border-bottom:1px solid var(--rule)}
.sv .nm{font-size:16px}
.sv .tr{position:relative;height:22px;background:linear-gradient(var(--rule),var(--rule)) left center/100% 1px no-repeat}
.sv .tr i{position:absolute;top:50%;transform:translate(-50%,-50%);width:13px;height:13px;display:block}
.sv .tr i.c{width:18px;height:18px;border-radius:50%;background:var(--hn);z-index:2;box-shadow:0 0 0 3px var(--paper)}
.sv .tr i.so{background:var(--ink)}
.sv .tr i.jb{background:var(--teal);transform:translate(-50%,-50%) rotate(45deg)}
.sv .tr i.pe{width:0;height:0;border-left:8px solid transparent;border-right:8px solid transparent;border-bottom:14px solid var(--ochre)}
.sv .tr b{position:absolute;top:-17px;font-family:var(--mono);font-size:11px;color:var(--hn-deep);transform:translateX(-50%)}
.sv.ax .tr{background:none}
.sv.ax .tr span{position:absolute;font-family:var(--mono);font-size:10.5px;color:var(--mute);transform:translateX(-50%)}
@media (max-width:900px){.srcgrid{grid-template-columns:1fr}.srcgrid > div{border-right:0;padding-left:0;border-bottom:1px solid var(--rule)}.sv{grid-template-columns:100px 1fr}}
'''
rep("/* model bars */", CSS + "/* model bars */")

# --- JS: hero/stats
rep("const qSum = D.n_comments;", "const qSum = D.n_read;")
rep("$('h-bigsub').textContent = `${cc.n} z ${N} autorov · 2,8× viac ako #2 Codex CLI`;",
    "$('h-bigsub').textContent = `${cc.n} z ${N} autorov · ${(cc.n / D.harness[1].n).toFixed(1).replace('.', ',')}× viac ako #2 ${D.harness[1].name}`;")
rep("[21+11,'zdrojov (vlákna + blogy)']", "[D.sources.length,'komunity a blogy']")
rep("// 1 harness", "const MED = (() => { const v = D.spend.slice().sort((a, b) => a - b), n = v.length; return (v[Math.floor((n-1)/2)] + v[Math.ceil((n-1)/2)]) / 2; })();\n$('h-med').textContent = '$' + Math.round(MED);\n$('n-art').textContent = D.n_blog_articles;\n$('n-auth-b').textContent = D.n_blog_authors;\n$('n-harn').textContent = D.n_harness_authors;\n// 1 harness")

# --- JS: trend quarter labels (2026 only, last partial)
rep("const ql = qs.map(q => q.split('-')[1] + \"’\" + q.slice(2, 4));", "const ql = qs.map(q => q + \"’26\");")
rep("${i===0||i===n-1?' (čiastočný)':''}", "${i===n-1?' (do 5. 11.)':''}")

# --- JS: new renderers before trend
NEWJS = r'''
// 2 sources heatmap
(function srcmap() {
  const B = D.by_source, rows = B.rows;
  let h = '<thead><tr><th></th>' + B.tools.map(t => `<th><span>${esc(t)}</span></th>`).join('') + '</tr></thead><tbody>';
  rows.forEach(r => { const mx = Math.max(...r.share, 1);
    h += `<tr><th>${esc(r.label)}<small>${r.n} autorov${r.n < 30 ? ' · malá vzorka' : ''}</small></th>` + r.share.map((v, i) => { const a = v / mx;
      return `<td class="${v === 0 ? 'z' : a > .55 ? 'hi' : ''}" style="--a:${(a * .95).toFixed(3)}" title="${esc(r.label)} · ${esc(B.tools[i])}: ${r.cnt[i]} z ${r.n} (${v} %)">${v === 0 ? '·' : Math.round(v)}</td>`; }).join('') + '</tr>'; });
  $('srcmap').innerHTML = h + '</tbody>';
  const g = (src, tool) => { const r = rows.find(x => x.src === src); return r ? r.share[B.tools.indexOf(tool)] : 0; };
  $('src-note').innerHTML = `Claude Code vedie všade (HN ${Math.round(g('hn','Claude Code'))} %, Lobste.rs ${Math.round(g('lobsters','Claude Code'))} %, Tildes ${Math.round(g('tildes','Claude Code'))} %). Rozdiely sú v chvoste: <b>HN</b> je baštou Codexu a open-source agentov (OpenCode ${Math.round(g('hn','OpenCode'))} %, Pi ${Math.round(g('hn','Pi'))} %). <b>Lobste.rs</b> častejšie používa chat (Claude app ${Math.round(g('lobsters','Claude (app/web)'))} %) a je skeptickejší. <b>Tildes</b> má najviac používateľov GitHub Copilot (${Math.round(g('tildes','GitHub Copilot'))} %).`;
})();

// 3 interfaces
(function ifaces() {
  const rows = D.iface.filter(r => r.n > 0), m = Math.max(...rows.map(r => r.n));
  $('b-iface').innerHTML = rows.map((r, i) => `<div class="bar mbar" style="--w:${(100*r.exp/m).toFixed(2)}%;--w2:${(100*(r.n-r.exp)/m).toFixed(2)}%;--d:${i*45}ms;--c:${r.id==='terminal'?'var(--hn)':'var(--ink)'}" title="${esc(r.name)}: ${r.exp} výslovne + ${r.n-r.exp} doplnené">
    <span class="bl">${esc(r.name)}</span><span class="bt"><i style="background:var(--c)"></i><b></b></span><span class="bn">${r.n}<small>${r.exp} výslovne</small></span></div>`).join('');
  bars('b-host', D.hosts.map(h => ({...h, name: h.name === 'browser' ? 'prehliadač' : h.name})), {c: 'var(--ink2)', sub: r => ''});
  const cc = D.tool_split['Claude Code'], ccn = cc.explicit.reduce((a, r) => a + r.n, 0);
  bars('b-ccsplit', cc.explicit, {c: 'var(--hn)', sub: r => Math.round(100 * r.n / ccn) + ' %'});
  $('cc-note').innerHTML = `Z <b>${cc.total}</b> používateľov Claude Code uviedlo rozhranie ${ccn} prípadov. Terminál jasne dominuje, no <b>desktop app</b> a <b>mobilná appka</b> (riadenie agenta z telefónu) už nie sú okrajové.`;
  const cp = D.tool_split['GitHub Copilot'], cpn = cp.explicit.reduce((a, r) => a + r.n, 0);
  bars('b-cpsplit', cp.explicit, {c: 'var(--sky)', sub: r => Math.round(100 * r.n / cpn) + ' %'});
  const Vm = D.via; const mx = Math.max(...Vm.m.flat());
  let h = '<thead><tr><th></th>' + Vm.vias.map(v => `<th><span>${esc(v === 'own scripts/API' ? 'vlastné skripty/API' : v)}</span></th>`).join('') + '<th><span>spolu</span></th></tr></thead><tbody>';
  Vm.models.forEach((g, i) => { h += `<tr><th>${esc(g)}</th>` + Vm.m[i].map((v, j) => { const a = v / mx;
    return `<td class="${v === 0 ? 'z' : a > .5 ? 'hi' : ''}" style="--a:${(Math.sqrt(a) * .95).toFixed(3)}" title="${esc(g)} cez ${esc(Vm.vias[j])}: ${v} autorov">${v || '·'}</td>`; }).join('') + `<td class="z" style="--a:0;font-weight:600;color:var(--ink)">${Vm.tot[i]}</td></tr>`; });
  $('viamap').innerHTML = h + '</tbody>';
})();
'''
rep("// 2 trend — small multiples, shared y scale", NEWJS + "\n// 2 trend — small multiples, shared y scale")

# --- JS: surveys + source summary replace threads
a = s.index("// 8 threads"); b = s.index("// reveal")
s = s[:a] + r'''// 9 surveys
(function surveys() {
  const S = D.surveys, MAX = 75, x = v => (100 * v / MAX).toFixed(2) + '%';
  let h = `<div class="sv ax"><span></span><div class="tr">${[0, 15, 30, 45, 60, 75].map(t => `<span style="left:${x(t)}">${t} %</span>`).join('')}</div></div>`;
  h += S.map(r => `<div class="sv"><span class="nm">${esc(r.name)}</span><div class="tr">
    ${r.so != null ? `<i class="so" style="left:${x(r.so)}" title="Stack Overflow: ${r.so} %"></i>` : ''}
    ${r.jb != null ? `<i class="jb" style="left:${x(r.jb)}" title="JetBrains: ${r.jb} %"></i>` : ''}
    ${r.pe != null ? `<i class="pe" style="left:${x(r.pe)}" title="Pragmatic Engineer: ${r.pe} %"></i>` : ''}
    <i class="c" style="left:${x(r.community)}" title="Komunita: ${r.community} %"></i><b style="left:${x(r.community)}">${Math.round(r.community)}</b></div></div>`).join('');
  $('surveys').innerHTML = h;
  $('s-leg').innerHTML = [['background:var(--hn)', 'Komunita (HN · Lobste.rs · Tildes · blogy)'], ['background:var(--ink);border-radius:0', 'Stack Overflow 2026'], ['background:var(--teal);border-radius:0;transform:rotate(45deg)', 'JetBrains 2026 (máj–júl)'], ['width:0;height:0;border-radius:0;background:none;border-left:7px solid transparent;border-right:7px solid transparent;border-bottom:12px solid var(--ochre)', 'Pragmatic Engineer 2026']]
    .map(([st, t]) => `<span><i style="${st}"></i>${t}</span>`).join('');
})();

// 11 sources summary
$('srcsum').innerHTML = D.src_summary.filter(s => s.id !== 'blogs').map(s => `<div><h3>${esc(s.label)}</h3>
  <div class="k">${s.threads} vlákien · ${nf(s.read)} komentárov · <b style="color:var(--ink)">${s.authors}</b> autorov so setupom</div>
  <div class="k">Top: ${s.top.map(([t, n]) => esc(t) + ' ' + n).join(' · ')}</div>
  <ol>${s.tt.map(t => `<li><a href="${esc(t.u)}" target="_blank" rel="noopener">${esc(t.t.replace(/^Ask HN: /, ''))}</a><small>${t.a} autorov</small></li>`).join('')}</ol></div>`).join('');

''' + s[b:]

open(f"{PIPE}/infographic_v2_tpl.html", "w").write(s)
print("template v2 written", len(s))
