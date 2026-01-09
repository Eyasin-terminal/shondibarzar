import React, { useState, useEffect } from 'react';
import { 
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, 
  PieChart, Pie, Cell, Radar, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis
} from 'recharts';
import { 
  BookOpen, Download, ChevronDown, Users, Smartphone, 
  Wifi, MapPin, ArrowRight, CheckCircle, Menu, X, Share2, Award
} from 'lucide-react';

// --- DATASET ---
const demographics = [
  { name: '20-30 Years', value: 65, fill: '#3b82f6' },
  { name: '31-40 Years', value: 25, fill: '#60a5fa' },
  { name: '41-50 Years', value: 8, fill: '#93c5fd' },
  { name: '50+ Years', value: 2, fill: '#bfdbfe' },
];

const constructComparison = [
  { name: 'Usefulness (PU)', rural: 4.5, city: 4.6 },
  { name: 'Ease of Use (PEOU)', rural: 4.2, city: 4.3 },
  { name: 'Intention (BI)', rural: 4.7, city: 4.8 },
  { name: 'Infrastructure (FC)', rural: 2.5, city: 4.2 },
  { name: 'Support (IS)', rural: 2.9, city: 3.8 },
];

const correlationData = [
  { name: 'Facilities', impact: 35 },
  { name: 'Ease of Use', impact: 55 },
  { name: 'Self-Efficacy', impact: 65 },
  { name: 'Usefulness', impact: 78 },
  { name: 'Attitude', impact: 85 },
];

// --- COMPONENTS ---

const Section = ({ id, className = "", children }) => (
  <section id={id} className={`py-20 px-6 md:px-12 max-w-7xl mx-auto ${className}`}>
    {children}
  </section>
);

const SectionTitle = ({ title, subtitle, align = "center" }) => (
  <div className={`mb-16 ${align === 'left' ? 'text-left' : 'text-center'}`}>
    <h2 className="text-3xl md:text-4xl font-bold text-slate-900 mb-4">{title}</h2>
    <div className={`h-1.5 w-24 bg-blue-600 rounded-full mb-6 ${align === 'left' ? '' : 'mx-auto'}`}></div>
    <p className="text-lg text-slate-600 max-w-2xl mx-auto">{subtitle}</p>
  </div>
);

const StatCard = ({ icon: Icon, value, label, subtext }) => (
  <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-100 hover:shadow-md transition-shadow text-center">
    <div className="bg-blue-50 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-6 text-blue-600">
      <Icon size={32} />
    </div>
    <h3 className="text-4xl font-bold text-slate-900 mb-2">{value}</h3>
    <p className="text-lg font-semibold text-slate-700 mb-2">{label}</p>
    <p className="text-sm text-slate-500">{subtext}</p>
  </div>
);

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 50);
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const handlePrint = () => {
    window.print();
  };

  return (
    <nav className={`fixed w-full z-50 transition-all duration-300 ${scrolled ? 'bg-white/90 backdrop-blur-md shadow-sm py-4' : 'bg-transparent py-6'} print:hidden`}>
      <div className="max-w-7xl mx-auto px-6 flex justify-between items-center">
        <div className="flex items-center gap-2">
          <BookOpen className={`w-8 h-8 ${scrolled ? 'text-blue-600' : 'text-slate-900'}`} />
          <span className={`text-xl font-bold tracking-tight ${scrolled ? 'text-slate-900' : 'text-slate-900'}`}>EduInsight BD</span>
        </div>
        
        <div className="hidden md:flex items-center gap-8">
          {['Findings', 'Demographics', 'Strategy', 'Report'].map((item) => (
            <a key={item} href={`#${item.toLowerCase()}`} className="text-sm font-medium text-slate-600 hover:text-blue-600 transition-colors">
              {item}
            </a>
          ))}
          <button 
            onClick={handlePrint}
            className="bg-slate-900 text-white px-5 py-2.5 rounded-full text-sm font-medium hover:bg-slate-800 transition-all flex items-center gap-2 cursor-pointer"
          >
            <Download size={16} /> Download PDF
          </button>
        </div>

        <button className="md:hidden text-slate-800" onClick={() => setIsOpen(!isOpen)}>
          {isOpen ? <X /> : <Menu />}
        </button>
      </div>

      {/* Mobile Menu */}
      {isOpen && (
        <div className="absolute top-full left-0 w-full bg-white border-b border-slate-100 p-6 md:hidden shadow-xl">
          <div className="flex flex-col gap-4">
            {['Findings', 'Demographics', 'Strategy', 'Report'].map((item) => (
              <a key={item} href={`#${item.toLowerCase()}`} onClick={() => setIsOpen(false)} className="text-lg font-medium text-slate-800">
                {item}
              </a>
            ))}
            <button 
              onClick={() => {
                handlePrint();
                setIsOpen(false);
              }}
              className="text-lg font-medium text-blue-600 flex items-center gap-2"
            >
              <Download size={20} /> Download PDF
            </button>
          </div>
        </div>
      )}
    </nav>
  );
};

export default function ResearchWebsite() {
  const [copied, setCopied] = useState(false);

  // Define handlePrint here for the footer button
  const handlePrint = () => {
    window.print();
  };

  const handleScrollToFindings = () => {
    const element = document.getElementById('findings');
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  const handleShare = () => {
    const dummy = document.createElement("input");
    document.body.appendChild(dummy);
    dummy.value = window.location.href;
    dummy.select();
    document.execCommand("copy");
    document.body.removeChild(dummy);
    
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="font-sans text-slate-900 bg-slate-50 overflow-x-hidden print:bg-white">
      <Navbar />

      {/* --- HERO SECTION --- */}
      <header className="relative pt-32 pb-20 lg:pt-48 lg:pb-32 px-6 overflow-hidden print:pt-10 print:pb-10">
        <div className="absolute top-0 right-0 -mr-20 -mt-20 w-96 h-96 bg-blue-200 rounded-full blur-3xl opacity-30 print:hidden"></div>
        <div className="absolute bottom-0 left-0 -ml-20 -mb-20 w-80 h-80 bg-indigo-200 rounded-full blur-3xl opacity-30 print:hidden"></div>

        <div className="max-w-4xl mx-auto text-center relative z-10">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-100 text-blue-700 text-xs font-bold uppercase tracking-wider mb-8 print:border print:border-blue-200">
            <Award size={14} /> National Research 2026
          </div>
          <h1 className="text-5xl md:text-7xl font-extrabold text-slate-900 leading-tight mb-8">
            Bridging the <br />
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-indigo-600 print:text-slate-900">
              Digital Divide
            </span> in Education
          </h1>
          <p className="text-xl md:text-2xl text-slate-600 leading-relaxed mb-10 max-w-2xl mx-auto">
            A comprehensive analysis of behavioral intention among rural primary school teachers in Bangladesh.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center print:hidden">
            <button 
              onClick={handleScrollToFindings}
              className="bg-blue-600 text-white px-8 py-4 rounded-full font-bold text-lg hover:bg-blue-700 transition-all shadow-lg shadow-blue-200 flex items-center justify-center gap-2 cursor-pointer"
            >
              Explore Findings <ArrowRight size={20} />
            </button>
            <button 
              onClick={handleShare}
              className="bg-white text-slate-700 border border-slate-200 px-8 py-4 rounded-full font-bold text-lg hover:bg-slate-50 transition-all flex items-center justify-center gap-2 cursor-pointer"
            >
              {copied ? <CheckCircle size={20} className="text-green-500" /> : <Share2 size={20} />} 
              {copied ? "Link Copied!" : "Share Report"}
            </button>
          </div>
        </div>
        
        <div className="absolute bottom-8 left-1/2 -translate-x-1/2 animate-bounce text-slate-400 print:hidden">
          <ChevronDown size={32} />
        </div>
      </header>

      {/* --- KEY STATS --- */}
      <section className="bg-white py-12 border-y border-slate-100">
        <div className="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          <StatCard icon={Users} value="150+" label="Teachers Surveyed" subtext="Across 12 Rural Districts" />
          <StatCard icon={CheckCircle} value="4.8/5" label="Adoption Readiness" subtext="High Behavioral Intention" />
          <StatCard icon={Smartphone} value="92%" label="Smartphone Reliance" subtext="Primary Digital Tool" />
          <StatCard icon={Wifi} value="-45%" label="Infrastructure Gap" subtext="Rural vs Urban Variance" />
        </div>
      </section>

      {/* --- THE GAP SECTION (Radar Chart) --- */}
      <Section id="findings">
        <SectionTitle 
          title="The Infrastructure Paradox" 
          subtitle="Teachers are mentally ready, but physically unequipped. While motivation is high across the board, rural schools lack the basic facilities to support this ambition."
        />
        
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <div className="bg-white p-6 rounded-3xl shadow-lg border border-slate-100 h-[500px] print:shadow-none print:border">
            <ResponsiveContainer width="100%" height="100%">
              <RadarChart cx="50%" cy="50%" outerRadius="80%" data={constructComparison}>
                <PolarGrid stroke="#e2e8f0" />
                <PolarAngleAxis dataKey="name" tick={{ fill: '#64748b', fontSize: 12 }} />
                <PolarRadiusAxis angle={30} domain={[0, 5]} />
                <Radar name="City Schools" dataKey="city" stroke="#3b82f6" fill="#3b82f6" fillOpacity={0.2} />
                <Radar name="Rural Schools" dataKey="rural" stroke="#ef4444" fill="#ef4444" fillOpacity={0.2} />
                <Legend />
                <Tooltip />
              </RadarChart>
            </ResponsiveContainer>
          </div>

          <div className="space-y-8">
            <div className="bg-blue-50 border-l-4 border-blue-500 p-6 rounded-r-xl print:bg-white print:border-l-2 print:border-slate-300">
              <h4 className="text-xl font-bold text-blue-900 mb-2">The Critical Insight</h4>
              <p className="text-blue-800 leading-relaxed print:text-slate-800">
                Look at the sharp drop in <strong>"Infrastructure (FC)"</strong> and <strong>"Support (IS)"</strong> for Rural schools (Red). Yet, <strong>"Intention (BI)"</strong> remains nearly identical to City schools. Rural teachers are resilient, overcoming physical barriers with personal motivation.
              </p>
            </div>
            
            <div>
              <h4 className="text-lg font-bold text-slate-900 mb-4">Why this matters:</h4>
              <ul className="space-y-4">
                {[
                  "Government investments are currently skewed towards urban centers.",
                  "Rural teachers are substituting missing labs with personal smartphones.",
                  "Tech anxiety is surprisingly low, disproving the 'technophobe' myth."
                ].map((item, i) => (
                  <li key={i} className="flex items-start gap-3">
                    <div className="mt-1 min-w-[20px] h-5 bg-green-100 rounded-full flex items-center justify-center text-green-600 print:bg-slate-100 print:text-slate-800">
                      <CheckCircle size={12} />
                    </div>
                    <span className="text-slate-600">{item}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </Section>

      {/* --- DRIVERS OF ADOPTION (Bar/Area) --- */}
      <section className="bg-slate-900 py-24 text-white print:bg-white print:text-slate-900">
        <div className="max-w-7xl mx-auto px-6">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-16">
            <div>
              <h2 className="text-3xl md:text-4xl font-bold mb-6">What actually drives adoption?</h2>
              <p className="text-slate-400 text-lg mb-8 leading-relaxed print:text-slate-600">
                We ran a multiple regression analysis to identify which factors actually predict a teacher's intention to use digital tools. The results were surprising: <strong>Usefulness</strong> trumps <strong>Ease of Use</strong>.
              </p>
              
              <div className="space-y-6">
                {correlationData.map((item, i) => (
                  <div key={i}>
                    <div className="flex justify-between text-sm mb-2 font-medium">
                      <span>{item.name}</span>
                      <span className="text-blue-400 print:text-blue-600">{item.impact}% Impact</span>
                    </div>
                    <div className="w-full bg-slate-800 rounded-full h-2 print:bg-slate-200">
                      <div 
                        className="bg-gradient-to-r from-blue-600 to-indigo-500 h-2 rounded-full transition-all duration-1000 print:bg-blue-600" 
                        style={{ width: `${item.impact}%` }}
                      ></div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
            
            <div className="relative">
              <div className="absolute inset-0 bg-blue-500 rounded-full blur-[100px] opacity-20 print:hidden"></div>
              <div className="relative bg-slate-800 p-8 rounded-3xl border border-slate-700 h-96 print:bg-white print:border-slate-200">
                <h3 className="text-lg font-bold mb-6 text-slate-200 print:text-slate-800">Adoption Drivers (Regression Coefficients)</h3>
                <ResponsiveContainer width="100%" height="100%">
                  <BarChart data={correlationData} layout="vertical" margin={{ left: 20, right: 20, bottom: 20 }}>
                    <XAxis type="number" hide />
                    <YAxis dataKey="name" type="category" width={100} tick={{ fill: '#94a3b8' }} />
                    <Tooltip contentStyle={{ backgroundColor: '#1e293b', borderColor: '#334155', color: '#fff' }} />
                    <Bar dataKey="impact" fill="#3b82f6" radius={[0, 4, 4, 0]} barSize={30}>
                      {correlationData.map((entry, index) => (
                        <Cell key={`cell-${index}`} fill={['#ef4444', '#f59e0b', '#3b82f6', '#6366f1', '#8b5cf6'][index]} />
                      ))}
                    </Bar>
                  </BarChart>
                </ResponsiveContainer>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* --- DEMOGRAPHICS (Pie) --- */}
      <Section id="demographics">
        <SectionTitle 
          title="A Young, Ready Workforce" 
          subtitle="The demographic analysis reveals a 'Digital Native' teacher cohort. The stereotypical image of an aging, resistant workforce is outdated."
        />
        
        <div className="bg-white p-8 md:p-12 rounded-3xl shadow-sm border border-slate-100 print:shadow-none print:border-slate-200">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
            <div className="h-80">
              <ResponsiveContainer width="100%" height="100%">
                <PieChart>
                  <Pie 
                    data={demographics} 
                    innerRadius={80} 
                    outerRadius={120} 
                    paddingAngle={5} 
                    dataKey="value"
                  >
                    {demographics.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={entry.fill} />
                    ))}
                  </Pie>
                  <Tooltip />
                  <Legend verticalAlign="bottom" height={36}/>
                </PieChart>
              </ResponsiveContainer>
            </div>

            <div>
              <h3 className="text-2xl font-bold text-slate-900 mb-4">65% are under 30 Years Old</h3>
              <p className="text-slate-600 mb-6 leading-relaxed">
                The vast majority of respondents belong to the Millennial or Gen-Z cohorts. These teachers grew up with technology. They don't need "basic computer literacy" training; they need <strong>pedagogical integration</strong> training.
              </p>
              <div className="grid grid-cols-2 gap-4">
                <div className="bg-blue-50 p-4 rounded-xl print:bg-white print:border print:border-blue-100">
                  <div className="text-2xl font-bold text-blue-600 mb-1">Low</div>
                  <div className="text-sm text-slate-600 font-medium">Tech Anxiety</div>
                </div>
                <div className="bg-indigo-50 p-4 rounded-xl print:bg-white print:border print:border-indigo-100">
                  <div className="text-2xl font-bold text-indigo-600 mb-1">High</div>
                  <div className="text-sm text-slate-600 font-medium">Adaptability</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </Section>

      {/* --- STRATEGY CARDS --- */}
      <Section id="strategy" className="bg-white">
        <SectionTitle 
          title="Strategic Roadmap" 
          subtitle="Actionable policy recommendations based on the data evidence." 
          align="center"
        />

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {/* Strategy 1 */}
          <div className="group relative bg-slate-50 rounded-2xl p-8 transition-all hover:-translate-y-2 hover:shadow-xl border border-slate-100 print:bg-white print:border-slate-200">
            <div className="absolute top-0 right-0 p-6 opacity-10 group-hover:opacity-20 transition-opacity">
              <Smartphone size={100} className="text-blue-600" />
            </div>
            <div className="w-12 h-12 bg-blue-600 rounded-lg flex items-center justify-center text-white mb-6">1</div>
            <h3 className="text-xl font-bold text-slate-900 mb-3">The "BYOD" Policy</h3>
            <p className="text-slate-600 mb-6">
              Rural teachers are already using personal phones. Formalize this by providing data subsidies and educational apps optimized for mobile, rather than waiting for expensive PC labs.
            </p>
            <a href="#" className="text-blue-600 font-bold text-sm flex items-center gap-1">Read Proposal <ArrowRight size={14} /></a>
          </div>

          {/* Strategy 2 */}
          <div className="group relative bg-slate-50 rounded-2xl p-8 transition-all hover:-translate-y-2 hover:shadow-xl border border-slate-100 print:bg-white print:border-slate-200">
            <div className="absolute top-0 right-0 p-6 opacity-10 group-hover:opacity-20 transition-opacity">
              <BookOpen size={100} className="text-indigo-600" />
            </div>
            <div className="w-12 h-12 bg-indigo-600 rounded-lg flex items-center justify-center text-white mb-6">2</div>
            <h3 className="text-xl font-bold text-slate-900 mb-3">Impact over Ease</h3>
            <p className="text-slate-600 mb-6">
              Stop training on "how to turn it on." Focus training on "how it improves grades." Perceived Usefulness is the #1 driver of adoption, not Ease of Use.
            </p>
            <a href="#" className="text-indigo-600 font-bold text-sm flex items-center gap-1">View Curriculum <ArrowRight size={14} /></a>
          </div>

          {/* Strategy 3 */}
          <div className="group relative bg-slate-50 rounded-2xl p-8 transition-all hover:-translate-y-2 hover:shadow-xl border border-slate-100 print:bg-white print:border-slate-200">
            <div className="absolute top-0 right-0 p-6 opacity-10 group-hover:opacity-20 transition-opacity">
              <MapPin size={100} className="text-purple-600" />
            </div>
            <div className="w-12 h-12 bg-purple-600 rounded-lg flex items-center justify-center text-white mb-6">3</div>
            <h3 className="text-xl font-bold text-slate-900 mb-3">Rural Infrastructure Kit</h3>
            <p className="text-slate-600 mb-6">
              Standardize a "Low-Cost Kit" (1 Laptop + 1 Projector + 4G Modem) for rural schools to immediately bridge the Facilitating Conditions gap.
            </p>
            <a href="#" className="text-purple-600 font-bold text-sm flex items-center gap-1">See Costing <ArrowRight size={14} /></a>
          </div>
        </div>
      </Section>

      {/* --- FOOTER --- */}
      <footer className="bg-slate-900 text-slate-400 py-16 print:bg-white print:text-slate-600">
        <div className="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-4 gap-12">
          <div className="col-span-1 md:col-span-2">
            <div className="flex items-center gap-2 mb-6">
              <BookOpen className="text-blue-500" />
              <span className="text-xl font-bold text-white print:text-slate-900">EduInsight BD</span>
            </div>
            <p className="max-w-md">
              Advancing education through data-driven policy making. This research was conducted to understand the digital readiness of primary education in Bangladesh.
            </p>
          </div>
          
          <div className="print:hidden">
            <h4 className="text-white font-bold mb-6">Research</h4>
            <ul className="space-y-4 text-sm">
              <li><a href="#" className="hover:text-blue-400">Methodology</a></li>
              <li><a href="#" className="hover:text-blue-400">Data Sources</a></li>
              <li><a href="#" className="hover:text-blue-400">Questionnaire</a></li>
            </ul>
          </div>

          <div className="print:hidden">
            <h4 className="text-white font-bold mb-6">Connect</h4>
            <ul className="space-y-4 text-sm">
              <li><button onClick={handlePrint} className="hover:text-blue-400 text-left">Download Full PDF</button></li>
              <li><a href="#" className="hover:text-blue-400">Contact Research Team</a></li>
              <li><a href="#" className="hover:text-blue-400">Government Portal</a></li>
            </ul>
          </div>
        </div>
        <div className="max-w-7xl mx-auto px-6 mt-16 pt-8 border-t border-slate-800 text-sm text-center print:border-slate-200">
          &copy; 2026 EduInsight Research Group. All rights reserved.
        </div>
      </footer>
    </div>
  );
}
