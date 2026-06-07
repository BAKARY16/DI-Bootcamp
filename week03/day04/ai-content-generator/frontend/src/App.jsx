import { useState } from 'react'
import DashboardTab       from './components/tabs/DashboardTab.jsx'
import UsersTab           from './components/tabs/UsersTab.jsx'
import RecommendationsTab from './components/tabs/RecommendationsTab.jsx'
import AnalyticsTab       from './components/tabs/AnalyticsTab.jsx'
import VisualizationsTab  from './components/tabs/VisualizationsTab.jsx'

const TABS = [
  { id: 'dashboard',       label: 'Dashboard' },
  { id: 'users',           label: 'Utilisateurs' },
  { id: 'recommandations', label: 'Recommandations' },
  { id: 'analyse',         label: 'Analyse' },
  { id: 'visualisations',  label: 'Visualisations' },
]

const styles = {
  shell: { minHeight: '100vh', display: 'flex', flexDirection: 'column' },
  header: {
    display: 'flex', alignItems: 'center', gap: 12,
    padding: '14px 24px', background: '#fff',
    borderBottom: '1px solid rgba(0,0,0,0.07)',
  },
  logo: {
    width: 34, height: 34, borderRadius: 9, background: '#7F77DD',
    display: 'flex', alignItems: 'center', justifyContent: 'center',
    fontSize: 18, color: '#fff', flexShrink: 0,
  },
  appName:  { fontSize: 15, fontWeight: 600, letterSpacing: '-0.3px' },
  appSub:   { fontSize: 11, color: '#73726c', fontFamily: 'monospace', marginTop: 1 },
  dot:      { width: 7, height: 7, borderRadius: '50%', background: '#1D9E75', marginLeft: 'auto' },
  dotLabel: { fontSize: 11, color: '#085041', fontFamily: 'monospace' },
  tabBar: {
    display: 'flex', background: '#fff',
    borderBottom: '1px solid rgba(0,0,0,0.07)', padding: '0 24px',
  },
  content: { flex: 1, padding: 24, maxWidth: 1100, margin: '0 auto', width: '100%' },
}

export default function App() {
  const [activeTab, setActiveTab] = useState('dashboard')

  return (
    <div style={styles.shell}>
      {/* Header */}
      <div style={styles.header}>
        <div style={styles.logo}>⬡</div>
        <div>
          <div style={styles.appName}>AI Content Generator</div>
          <div style={styles.appSub}>Système de recommandation personnalisée</div>
        </div>
        <div style={styles.dot} />
        <div style={styles.dotLabel}>backend actif</div>
      </div>

      {/* Onglets */}
      <div style={styles.tabBar}>
        {TABS.map(tab => (
          <TabButton
            key={tab.id}
            label={tab.label}
            active={activeTab === tab.id}
            onClick={() => setActiveTab(tab.id)}
          />
        ))}
      </div>

      {/* Contenu */}
      <div style={styles.content}>
        {activeTab === 'dashboard'       && <DashboardTab />}
        {activeTab === 'users'           && <UsersTab />}
        {activeTab === 'recommandations' && <RecommendationsTab />}
        {activeTab === 'analyse'         && <AnalyticsTab />}
        {activeTab === 'visualisations'  && <VisualizationsTab />}
      </div>
    </div>
  )
}

function TabButton({ label, active, onClick }) {
  return (
    <button
      onClick={onClick}
      style={{
        padding: '10px 16px', fontSize: 13, fontWeight: 500,
        background: 'none', border: 'none', cursor: 'pointer',
        color: active ? '#3C3489' : '#73726c',
        borderBottom: active ? '2px solid #7F77DD' : '2px solid transparent',
        marginBottom: -1, transition: 'color .15s',
      }}
    >
      {label}
    </button>
  )
}
