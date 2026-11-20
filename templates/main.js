'use strict';
document.documentElement.classList.add('js');
const EMAIL = {{ email | tojson }};
const dictionaries = {
  fr: {
    skip:'Aller au contenu',nav_about:'À propos',nav_teach:'Enseignement',nav_research:'Recherche',nav_tutoring:'Tutorat',nav_projects:'Projets',nav_journey:'Parcours',nav_contact:'Contact',
    hero_eyebrow:'DOCTORANT EN MATHÉMATIQUES · SHERBROOKE, QC',hero_title:'Explorer les idées.<br/><span>Transmettre les maths.</span>',
    hero_lead: {{ presentation_fr | tojson }},
    hero_cta_primary:'Découvrir mon enseignement',hero_cta_secondary:'Entrer en contact',hero_note:'Recherche rigoureuse. Enseignement accessible. Curiosité constante.',
    visual_research:'Géométrie & structures',strip_1:'GÉOMÉTRIE COMPLEXE',strip_2:'ENSEIGNEMENT UNIVERSITAIRE',strip_3:'GÉOMÉTRIE DE POISSON',strip_4:'MATHÉMATIQUES APPLIQUÉES',
    about_kicker:'À PROPOS',about_title:'Les mathématiques,<br/><em>une passion à partager.</em>',
    about_intro:"Je suis doctorant en mathématiques à l'Université de Sherbrooke. Mon travail de recherche explore la géométrie complexe et les structures de Poisson.",
    about_text:"Mon parcours m'a conduit du Togo au Sénégal, puis en France et au Canada. Partout, l'enseignement a conservé une place essentielle : rendre les idées précises, poser les bonnes questions et accompagner chaque étudiant vers l'autonomie.",
    about_tag1:'Recherche fondamentale',about_tag2:'Pédagogie',about_tag3:'Collaboration',
    teach_kicker:'ENSEIGNEMENT',teach_title:'Faire comprendre.<br/><em>Donner confiance.</em>',teach_intro:"Du secondaire à l'université, j'accompagne les étudiants dans la compréhension des concepts et la résolution de problèmes.",
    course_uni:'UNIVERSITÉ DE SHERBROOKE',course_role:"Auxiliaire d'enseignement",
    {% for c in cours %}cours_{{ c.id }}_titre: {{ c.titre_fr | tojson }}, cours_{{ c.id }}_description: {{ c.description_fr | tojson }},
    {% endfor %}
    course_secondary:'EXPÉRIENCE AU SECONDAIRE · TOGO',school_title:'Mathématiques, physique & chimie',
    school_desc: {{ enseignement_secondaire_fr | tojson }},
    school_pill:'Préparation de cours · Évaluation · Suivi',teaching_footer:"J'accorde une place centrale à la clarté des explications, à la pratique régulière et au raisonnement autonome.",
    research_kicker:'RECHERCHE',research_title:'Des questions<br/><em>au cœur de la géométrie.</em>',
    research_lead: {{ recherche_intro_fr | tojson }},
    research_link:'Échanger sur mes recherches <span aria-hidden="true">↗</span>',
    {% for r in recherches %}recherche_{{ r.id }}_titre: {{ r.titre_fr | tojson }}, recherche_{{ r.id }}_description: {{ r.description_fr | tojson }},
    {% endfor %}
    research_note:"Ces thèmes reflètent mes travaux actuels de recherche doctorale.",
    tutoring_kicker:'TUTORAT & ACCOMPAGNEMENT',tutoring_title:'Progresser en maths.<br/><em>À chaque étape.</em>',
    tutoring_intro:"Des compétences développées au secondaire et à l'université, pour aider à comprendre et à résoudre les problèmes.",
    {% for t in tutorat %}tutor_{{ t.id }}_niveau: {{ t.niveau_fr | tojson }}, tutor_{{ t.id }}_titre: {{ t.titre_fr | tojson }}, tutor_{{ t.id }}_description: {{ t.description_fr | tojson }},
    {% endfor %}
    tutor_note:"Pour une collaboration pédagogique ou une demande de tutorat, contactez-moi afin d'échanger sur les besoins et les disponibilités.",
    projects_kicker:'PROJETS PYTHON',projects_title:'Apprendre en<br/><em>construisant.</em>',
    projects_intro:"Des projets personnels qui relient la programmation, les mathématiques et l'informatique quantique.",
    {% for p in projets %}projet_{{ p.id }}_titre: {{ p.titre_fr | tojson }}, projet_{{ p.id }}_description: {{ p.description_fr | tojson }}, projet_{{ p.id }}_statut: {{ p.statut_fr | tojson }},
    {% endfor %}
    cv_kicker:'CURRICULUM VITÆ',cv_title:'Mon parcours<br/><em>en un document.</em>',
    cv_description:'Téléchargez le CV correspondant à votre besoin : enseignement au cégep ou tutorat en mathématiques.',
    {% for c in cvs %}cv_{{ loop.index }}_title: {{ c.titre_fr | tojson }},
    {% endfor %}
    journey_kicker:'PARCOURS',journey_title:'Un parcours,<br/><em>plusieurs horizons.</em>',journey_intro:'Quatre étapes, un même fil conducteur : approfondir les mathématiques et les transmettre.',
    {% for d in parcours %}parcours_{{ d.id }}_annees: {{ d.annees_fr | tojson }}, parcours_{{ d.id }}_titre: {{ d.titre_fr | tojson }}, parcours_{{ d.id }}_lieu: {{ d.lieu_fr | tojson }},
    {% endfor %}
    contact_kicker:'CONTACT',contact_title:'Travaillons sur<br/><em>de nouvelles idées.</em>',
    contact_text:"Pour un échange scientifique, une collaboration pédagogique ou une possibilité d'enseignement des mathématiques à temps partiel, écrivez-moi.",
    contact_email:"M'envoyer un courriel",contact_copy:'Copier mon adresse',footer_note:'Site personnel · Sherbrooke, Québec',back_to_top:'Retour en haut',
    copied:'Adresse courriel copiée !',copy_failed:'Copie impossible : ouvrez votre messagerie.',
    page_title: {{ titre_site | tojson }},menu_open:'Ouvrir le menu',menu_close:'Fermer le menu',dark_aria:'Activer le mode sombre',light_aria:'Activer le mode clair'
  },
  en: {
    skip:'Skip to content',nav_about:'About',nav_teach:'Teaching',nav_research:'Research',nav_tutoring:'Tutoring',nav_projects:'Projects',nav_journey:'Background',nav_contact:'Contact',
    hero_eyebrow:'PHD STUDENT IN MATHEMATICS · SHERBROOKE, QC',hero_title:'Explore ideas.<br/><span>Make math accessible.</span>',
    hero_lead: {{ presentation_en | tojson }},
    hero_cta_primary:'Explore my teaching',hero_cta_secondary:'Get in touch',hero_note:'Rigorous research. Accessible teaching. Lifelong curiosity.',
    visual_research:'Geometry & structures',strip_1:'COMPLEX GEOMETRY',strip_2:'UNIVERSITY TEACHING',strip_3:'POISSON GEOMETRY',strip_4:'APPLIED MATHEMATICS',
    about_kicker:'ABOUT',about_title:'Mathematics,<br/><em>a passion to share.</em>',
    about_intro:"I'm a PhD student in mathematics at Université de Sherbrooke, working on complex geometry and Poisson structures.",
    about_text:"My academic path has taken me from Togo to Senegal, France and Canada. Teaching has been a constant throughout: expressing ideas precisely, asking the right questions and helping students become independent problem-solvers.",
    about_tag1:'Fundamental research',about_tag2:'Teaching',about_tag3:'Collaboration',
    teach_kicker:'TEACHING',teach_title:'Build understanding.<br/><em>Inspire confidence.</em>',teach_intro:'From secondary school to university, I help students grasp concepts and develop strong problem-solving skills.',
    course_uni:'UNIVERSITÉ DE SHERBROOKE',course_role:'Teaching assistant',
    {% for c in cours %}cours_{{ c.id }}_titre: {{ c.titre_en | tojson }}, cours_{{ c.id }}_description: {{ c.description_en | tojson }},
    {% endfor %}
    course_secondary:'SECONDARY SCHOOL TEACHING · TOGO',school_title:'Mathematics, physics & chemistry',
    school_desc: {{ enseignement_secondaire_en | tojson }},
    school_pill:'Lesson planning · Assessment · Student support',teaching_footer:'I value clear explanations, regular practice and independent reasoning.',
    research_kicker:'RESEARCH',research_title:'Questions at<br/><em>the heart of geometry.</em>',
    research_lead: {{ recherche_intro_en | tojson }},
    research_link:'Discuss my research <span aria-hidden="true">↗</span>',
    {% for r in recherches %}recherche_{{ r.id }}_titre: {{ r.titre_en | tojson }}, recherche_{{ r.id }}_description: {{ r.description_en | tojson }},
    {% endfor %}
    research_note:'These themes reflect my current doctoral research.',
    tutoring_kicker:'TUTORING & SUPPORT',tutoring_title:'Grow your skills.<br/><em>One step at a time.</em>',
    tutoring_intro:'Experience supporting learners from secondary school through university-level mathematics.',
    {% for t in tutorat %}tutor_{{ t.id }}_niveau: {{ t.niveau_en | tojson }}, tutor_{{ t.id }}_titre: {{ t.titre_en | tojson }}, tutor_{{ t.id }}_description: {{ t.description_en | tojson }},
    {% endfor %}
    tutor_note:'For teaching collaborations or tutoring enquiries, please get in touch to discuss needs and availability.',
    projects_kicker:'PYTHON PROJECTS',projects_title:'Learning by<br/><em>building.</em>',
    projects_intro:'Personal projects connecting programming, mathematics and quantum computing.',
    {% for p in projets %}projet_{{ p.id }}_titre: {{ p.titre_en | tojson }}, projet_{{ p.id }}_description: {{ p.description_en | tojson }}, projet_{{ p.id }}_statut: {{ p.statut_en | tojson }},
    {% endfor %}
    cv_kicker:'CURRICULUM VITAE',cv_title:'My experience,<br/><em>at a glance.</em>',
    cv_description:'Download the CV that best matches your needs: college teaching or mathematics tutoring.',
    {% for c in cvs %}cv_{{ loop.index }}_title: {{ c.titre_en | tojson }},
    {% endfor %}
    journey_kicker:'BACKGROUND',journey_title:'One journey,<br/><em>many horizons.</em>',journey_intro:'Four milestones, one thread: learning mathematics deeply and sharing it with others.',
    {% for d in parcours %}parcours_{{ d.id }}_annees: {{ d.annees_en | tojson }}, parcours_{{ d.id }}_titre: {{ d.titre_en | tojson }}, parcours_{{ d.id }}_lieu: {{ d.lieu_en | tojson }},
    {% endfor %}
    contact_kicker:'CONTACT',contact_title:'Let’s explore<br/><em>new ideas together.</em>',
    contact_text:'For research discussions, teaching collaborations or part-time mathematics teaching opportunities, feel free to reach out.',
    contact_email:'Send an email',contact_copy:'Copy my email',footer_note:'Personal website · Sherbrooke, Québec',back_to_top:'Back to top',
    copied:'Email address copied!',copy_failed:'Unable to copy. Please use the email link.',
    page_title:'Adji Madjou — Mathematics, research & teaching',menu_open:'Open menu',menu_close:'Close menu',dark_aria:'Switch to dark mode',light_aria:'Switch to light mode'
  }
};
function safePref(key, fallback) { try { return localStorage.getItem(key) || fallback; } catch { return fallback; } }
function savePref(key,val) { try { localStorage.setItem(key,val); } catch {} }
let lang = safePref('am-language','fr') === 'en' ? 'en' : 'fr';
let theme = safePref('am-theme','light') === 'dark' ? 'dark' : 'light';
const themeBtn=document.querySelector('.theme-toggle');
const langBtn=document.querySelector('#lang-toggle');
const menuBtn=document.querySelector('#menu-toggle');
const mobileNav=document.querySelector('#mobile-nav');
function setTheme(next) { theme=next; document.documentElement.dataset.theme=theme; savePref('am-theme',theme); const m=document.querySelector('meta[name="theme-color"]'); if(m)m.content=theme==='light'?'#f7f9fc':'#0b1425'; themeBtn.setAttribute('aria-label',dictionaries[lang][theme==='light'?'dark_aria':'light_aria']); }
function setLanguage(next) { lang=next; document.documentElement.lang=lang==='fr'?'fr':'en'; savePref('am-language',lang); document.querySelectorAll('[data-i18n]').forEach(el=>{const key=el.dataset.i18n;if(dictionaries[lang][key])el.textContent=dictionaries[lang][key];}); document.querySelectorAll('[data-i18n-html]').forEach(el=>{const key=el.dataset.i18nHtml;if(dictionaries[lang][key])el.innerHTML=dictionaries[lang][key];}); langBtn.innerHTML=lang==='fr'?'EN <span aria-hidden="true">↗</span>':'FR <span aria-hidden="true">↗</span>'; langBtn.setAttribute('aria-label',lang==='fr'?'Switch language to English':'Passer en français'); document.title=dictionaries[lang].page_title; setTheme(theme); menuBtn.setAttribute('aria-label',dictionaries[lang][mobileNav.hidden?'menu_open':'menu_close']); }
langBtn.addEventListener('click',()=>setLanguage(lang==='fr'?'en':'fr'));
themeBtn.addEventListener('click',()=>setTheme(theme==='light'?'dark':'light'));
function setMenu(open){ mobileNav.hidden=!open; menuBtn.setAttribute('aria-expanded',String(open)); menuBtn.setAttribute('aria-label',dictionaries[lang][open?'menu_close':'menu_open']); document.body.classList.toggle('menu-open',open); }
menuBtn.addEventListener('click',()=>setMenu(mobileNav.hidden));
mobileNav.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>setMenu(false)));
window.addEventListener('resize',()=>{if(innerWidth>1080 && !mobileNav.hidden)setMenu(false);});
const toast=document.querySelector('#toast');
let toastHandle;
function showToast(text){toast.textContent=text;toast.classList.add('show');clearTimeout(toastHandle);toastHandle=setTimeout(()=>toast.classList.remove('show'),3200);}
document.querySelector('#copy-email').addEventListener('click',async()=>{try{if(!navigator.clipboard)throw Error('clipboard unavailable');await navigator.clipboard.writeText(EMAIL);showToast(dictionaries[lang].copied);}catch{showToast(dictionaries[lang].copy_failed);}});
document.querySelector('#year').textContent=String(new Date().getFullYear());
setLanguage(lang);
if('IntersectionObserver' in window) {
  const io=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('visible');io.unobserve(entry.target);}}),{threshold:.09,rootMargin:'0px 0px -10px 0px'});
  document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
  const navObserver=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){document.querySelectorAll('.nav-link').forEach(a=>a.classList.toggle('is-active',a.hash==='#'+entry.target.id));}}),{rootMargin:'-26% 0px -62% 0px'});
  document.querySelectorAll('section[id]').forEach(el=>navObserver.observe(el));
} else document.querySelectorAll('.reveal').forEach(el=>el.classList.add('visible'));
