'use client';

import React from 'react';
import { useLanguage } from '../context/LanguageContext';
import {
  BookOpen,
  GraduationCap,
  Timer,
  AlertTriangle,
  BarChart3,
  ShieldCheck,
  Globe,
  Wrench,
  Menu,
  X
} from 'lucide-react';

interface NavbarProps {
  activeTab: string;
  setActiveTab: (tab: string) => void;
  wrongCount: number;
}

export const Navbar: React.FC<NavbarProps> = ({
  activeTab,
  setActiveTab,
  wrongCount,
}) => {
  const { language, toggleLanguage, t } = useLanguage();
  const [mobileMenuOpen, setMobileMenuOpen] = React.useState(false);

  const mainNavItems = [
    { id: 'chapters', label: t('tabChapters'), shortLabel: language === 'zh' ? '章節' : 'Chapters', icon: BookOpen },
    { id: 'units', label: t('tabUnits'), shortLabel: language === 'zh' ? '單元' : 'Units', icon: GraduationCap },
    { id: 'mock', label: t('tabMock'), shortLabel: language === 'zh' ? '模考' : 'Mock', icon: Timer },
    {
      id: 'wrong',
      label: t('tabWrong'),
      shortLabel: language === 'zh' ? '錯題' : 'Mistakes',
      icon: AlertTriangle,
      badge: wrongCount > 0 ? wrongCount : undefined,
    },
    { id: 'analytics', label: t('tabAnalytics'), shortLabel: language === 'zh' ? '分析' : 'Stats', icon: BarChart3 },
    { id: 'cms', label: t('tabCMS'), shortLabel: language === 'zh' ? '審核' : 'CMS', icon: ShieldCheck },
  ];

  const handleTabClick = (id: string) => {
    setActiveTab(id);
    setMobileMenuOpen(false);
  };

  return (
    <>
      {/* Top Header */}
      <header className="bg-slate-900 border-b border-slate-800 text-slate-100 sticky top-0 z-40 shadow-md">
        <div className="max-w-7xl mx-auto px-3 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-14 sm:h-16">
            {/* Logo & Platform Info */}
            <div
              onClick={() => handleTabClick('chapters')}
              className="flex items-center space-x-2.5 cursor-pointer group select-none"
            >
              <div className="w-8 h-8 sm:w-9 sm:h-9 rounded-lg bg-cyan-600/20 border border-cyan-500/30 flex items-center justify-center text-cyan-400 group-hover:bg-cyan-600/30 transition-colors shrink-0">
                <Wrench className="w-4 h-4 sm:w-5 sm:h-5" />
              </div>
              <div>
                <div className="flex items-center space-x-1.5">
                  <span className="font-bold tracking-tight text-white text-sm sm:text-base">
                    {t('platformTitle')}
                  </span>
                  <span className="text-[10px] font-mono uppercase bg-cyan-950 text-cyan-300 px-1.5 py-0.2 rounded border border-cyan-800 hidden xs:inline-block">
                    C&G L2/3
                  </span>
                </div>
                <p className="text-[11px] text-slate-400 hidden sm:block truncate max-w-xs">
                  {t('platformSub')}
                </p>
              </div>
            </div>

            {/* Quick Actions (Bilingual Toggle + Mobile Drawer Toggle) */}
            <div className="flex items-center space-x-2">
              {/* Bilingual Switch Button */}
              <button
                onClick={toggleLanguage}
                className="flex items-center space-x-1.5 px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 active:scale-95 border border-slate-700 text-slate-200 text-xs font-medium transition shadow-sm"
                title="Toggle English / 繁中"
              >
                <Globe className="w-3.5 h-3.5 text-cyan-400" />
                <span className="font-mono text-xs">{language === 'zh' ? '繁中' : 'EN'}</span>
                <span className="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-pulse"></span>
              </button>

              {/* Mobile Drawer Trigger (More Options) */}
              <button
                onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
                className="p-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 md:hidden border border-slate-700"
                aria-label="Toggle navigation menu"
              >
                {mobileMenuOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
              </button>
            </div>
          </div>

          {/* Desktop Navigation Tabs (Hidden on Mobile) */}
          <nav className="hidden md:flex space-x-2 overflow-x-auto py-2 border-t border-slate-800/80 text-sm">
            {mainNavItems.map((item) => {
              const Icon = item.icon;
              const isActive = activeTab === item.id;
              return (
                <button
                  key={item.id}
                  onClick={() => handleTabClick(item.id)}
                  className={`flex items-center space-x-2 px-3 py-1.5 rounded-md text-xs sm:text-sm font-medium transition whitespace-nowrap ${
                    isActive
                      ? 'bg-cyan-600 text-white shadow-sm'
                      : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800'
                  }`}
                >
                  <Icon className="w-4 h-4" />
                  <span>{item.label}</span>
                  {item.badge !== undefined && (
                    <span
                      className={`ml-1 text-[11px] px-1.5 py-0.2 rounded-full font-bold ${
                        isActive
                          ? 'bg-rose-500 text-white'
                          : 'bg-rose-500/20 text-rose-300 border border-rose-500/30'
                      }`}
                    >
                      {item.badge}
                    </span>
                  )}
                </button>
              );
            })}
          </nav>
        </div>

        {/* Mobile Dropdown Menu (When hamburger tapped) */}
        {mobileMenuOpen && (
          <div className="md:hidden border-t border-slate-800 bg-slate-900/98 backdrop-blur px-4 py-3 space-y-1 shadow-2xl animate-in slide-in-from-top-2 duration-150">
            {mainNavItems.map((item) => {
              const Icon = item.icon;
              const isActive = activeTab === item.id;
              return (
                <button
                  key={item.id}
                  onClick={() => handleTabClick(item.id)}
                  className={`w-full flex items-center justify-between px-3 py-2.5 rounded-lg text-xs font-semibold transition ${
                    isActive
                      ? 'bg-cyan-600 text-white'
                      : 'text-slate-300 hover:bg-slate-800'
                  }`}
                >
                  <div className="flex items-center space-x-2.5">
                    <Icon className="w-4 h-4" />
                    <span>{item.label}</span>
                  </div>
                  {item.badge !== undefined && (
                    <span className="text-[10px] px-2 py-0.5 rounded-full font-bold bg-rose-500 text-white">
                      {item.badge}
                    </span>
                  )}
                </button>
              );
            })}
          </div>
        )}
      </header>

      {/* Mobile-First Fixed Bottom Navigation Bar (Thumb Friendly) */}
      <nav className="md:hidden fixed bottom-0 left-0 right-0 z-40 bg-slate-900/95 backdrop-blur-md border-t border-slate-800 px-2 py-1 shadow-2xl safe-area-inset-bottom">
        <div className="grid grid-cols-5 gap-1">
          {mainNavItems.slice(0, 5).map((item) => {
            const Icon = item.icon;
            const isActive = activeTab === item.id;
            return (
              <button
                key={item.id}
                onClick={() => handleTabClick(item.id)}
                className={`flex flex-col items-center justify-center py-1.5 px-1 rounded-lg text-[10px] font-medium transition relative active:scale-95 ${
                  isActive ? 'text-cyan-400 font-bold' : 'text-slate-400 hover:text-slate-200'
                }`}
              >
                <div className="relative">
                  <Icon className={`w-5 h-5 mb-0.5 ${isActive ? 'stroke-[2.5]' : 'stroke-[1.75]'}`} />
                  {item.badge !== undefined && (
                    <span className="absolute -top-1 -right-2 min-w-[14px] h-[14px] px-1 rounded-full text-[9px] font-bold bg-rose-500 text-white flex items-center justify-center leading-none">
                      {item.badge}
                    </span>
                  )}
                </div>
                <span className="truncate max-w-[56px] leading-tight mt-0.5">{item.shortLabel}</span>
                {isActive && (
                  <span className="w-3.5 h-0.5 rounded-full bg-cyan-400 absolute bottom-0.5"></span>
                )}
              </button>
            );
          })}
        </div>
      </nav>
    </>
  );
};
