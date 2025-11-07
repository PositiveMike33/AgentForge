#!/usr/bin/env python3
"""
Example usage of the ROI Automation System

This script demonstrates how to use the three specialist agents and the master
orchestration cog for AI automation ROI prioritization.

Author: AgentForge Community
Version: 1.0.0
Date: 2025-11-07
"""

from agentforge.agent import Agent
from agentforge.cog import Cog
import json
from datetime import datetime


# ==============================================================================
# Example 1: Using the Master Orchestration Cog (Recommended)
# ==============================================================================

def example_master_cog():
    """
    The master cog automatically routes requests to the appropriate specialist
    agent based on the user's input.
    """
    print("=" * 80)
    print("Example 1: Master Orchestration Cog")
    print("=" * 80)

    # Initialize the master cog
    roi_cog = Cog('roi_automation_master')

    # Example request: Revenue focus
    user_request = """
    I'm currently working at Labatt (15h-23h shift) and want to transition to
    full-time AI freelancing. I need to make $4000 CAD every 2 weeks to match
    my current income. I have 5 AI certifications and strong prompt engineering
    skills. I live in Montreal and can work in both French and English.
    """

    print(f"\nUser Request:\n{user_request}\n")
    print("Processing with ROI Automation Master Cog...\n")

    # Run the cog
    result = roi_cog.run(user_input=user_request)

    print("\n" + "=" * 80)
    print("Result:")
    print("=" * 80)
    print(result)


# ==============================================================================
# Example 2: Direct Agent Usage - Montreal Revenue Extractor
# ==============================================================================

def example_revenue_extractor():
    """
    Direct usage of the Montreal Revenue Extractor agent for detailed
    market analysis and client acquisition strategies.
    """
    print("\n" + "=" * 80)
    print("Example 2: Montreal Revenue Extractor (Direct)")
    print("=" * 80)

    # Initialize the agent
    revenue_agent = Agent('montreal_revenue_extractor')

    # Prepare parameters
    params = {
        'current_skills': "Prompt engineering, AI automation, Python, LangChain, AgentForge",
        'target_income': 4000,  # CAD per 2 weeks
        'available_hours': 20,  # Hours per week available for freelancing
        'current_employment': "Operator at Labatt, 15h-23h shift",
        'additional_context': """
        - 5 Coursera AI certifications
        - Based in Montreal (bilingual FR/EN)
        - Experience with GPT-4, Claude, local models
        - Interest in helping SMBs automate workflows
        """
    }

    print("\nRunning analysis...")
    result = revenue_agent.run(**params)

    # Parse JSON result
    analysis = json.loads(result) if isinstance(result, str) else result

    print("\n" + "=" * 80)
    print("Market Analysis:")
    print("=" * 80)
    print(json.dumps(analysis.get('market_analysis', {}), indent=2))

    print("\n" + "=" * 80)
    print("Service Packages:")
    print("=" * 80)
    print(json.dumps(analysis.get('service_packages', {}), indent=2))

    print("\n" + "=" * 80)
    print("21-Day Acquisition Pipeline:")
    print("=" * 80)
    pipeline = analysis.get('acquisition_pipeline', {})
    for week, tasks in pipeline.items():
        print(f"\n{week.upper()}:")
        for task in tasks:
            print(f"  - {task}")


# ==============================================================================
# Example 3: Direct Agent Usage - Productivity Optimizer
# ==============================================================================

def example_productivity_optimizer():
    """
    Direct usage of the Neuroscientific Productivity Optimizer agent for
    personalized performance enhancement protocols.
    """
    print("\n" + "=" * 80)
    print("Example 3: Neuroscientific Productivity Optimizer (Direct)")
    print("=" * 80)

    # Initialize the agent
    productivity_agent = Agent('productivity_optimizer')

    # Prepare parameters
    params = {
        'work_schedule': "15:00-23:00 weekdays (Labatt shift)",
        'sleep_pattern': "01:00-09:00",
        'wake_time': "09:00",
        'energy_peaks': "Morning after waking (09:30-11:30), Late afternoon (16:00-18:00)",
        'energy_troughs': "Post-lunch (13:00-14:30), Late evening (21:00-23:00)",
        'procrastination_triggers': "Complex projects without clear structure, administrative tasks, cold emailing",
        'focus_difficulties': "Context switching between Labatt work and freelance projects",
        'sleep_quality': "7/10 - Sometimes disrupted by shift work",
        'primary_goal': "Transition to full-time freelancing within 6 months while maintaining current income",
        'deep_work_hours': 4,  # Target hours per day
        'transition_timeline': "6 months",
        'dietary_restrictions': "None",
        'medical_conditions': "None",
        'supplement_budget': 100,  # CAD per month
        'additional_context': """
        - Night owl chronotype due to shift work
        - Need to balance current job with building freelance business
        - Want to maximize limited free time (mornings and weekends)
        """
    }

    print("\nGenerating personalized productivity protocol...")
    result = productivity_agent.run(**params)

    # Parse JSON result
    protocol = json.loads(result) if isinstance(result, str) else result

    print("\n" + "=" * 80)
    print("Chronobiological Analysis:")
    print("=" * 80)
    print(json.dumps(protocol.get('chronobiological_analysis', {}), indent=2))

    print("\n" + "=" * 80)
    print("Neurochemical Optimization Stack:")
    print("=" * 80)
    morning_stack = protocol.get('neurochemical_optimization', {}).get('morning_stack', [])
    for item in morning_stack[:3]:  # Show first 3 interventions
        print(f"\n{item.get('supplement', item.get('practice', 'Intervention'))}")
        print(f"  Purpose: {item.get('purpose')}")
        print(f"  Evidence: {item.get('evidence')}")


# ==============================================================================
# Example 4: Direct Agent Usage - GraphRAG Architect
# ==============================================================================

def example_graphrag_architect():
    """
    Direct usage of the GraphRAG Architect agent for knowledge management
    system design.
    """
    print("\n" + "=" * 80)
    print("Example 4: GraphRAG Knowledge Management Architect (Direct)")
    print("=" * 80)

    # Initialize the agent
    graphrag_agent = Agent('graphrag_architect')

    # Prepare parameters
    params = {
        'data_sources': [
            "Gmail (5 years of emails, ~50,000 messages)",
            "Google Drive (200GB documents, PDFs, presentations)",
            "Notion (500 notes on AI, freelancing, projects)",
            "GitHub (20 repositories, code and documentation)",
            "Coursera (5 AI certification materials)",
            "Browser bookmarks (1000+ AI resources)"
        ],
        'document_count': "~60,000",
        'data_size_gb': "220",
        'monthly_growth': "~2GB, 500 new documents",
        'monthly_budget': 500,  # USD
        'setup_budget': 200,  # USD one-time
        'maintenance_hours': 2,  # hours per week
        'cloud_preference': "AWS or GCP",
        'self_hosting': "Comfortable with Docker, basic DevOps",
        'programming_level': "Intermediate Python, familiar with APIs",
        'use_cases': [
            "Research past projects and client work for proposals",
            "Find relevant AI techniques and tools for specific problems",
            "Track learning progress and identify knowledge gaps",
            "Generate context-aware prompts for new projects",
            "Decision support with historical data"
        ],
        'queries_per_day': "20-30",
        'acceptable_latency': "<2 seconds",
        'accuracy_requirements': "85%+ relevant results in top 5",
        'data_sensitivity': "Medium (no passwords/API keys, but personal correspondence)",
        'compliance_requirements': "None specific, but GDPR-aware practices preferred",
        'third_party_sharing': "No - all data stays in personal infrastructure",
        'additional_context': """
        - Need fast retrieval for client calls and proposals
        - Want to learn from past successes and failures
        - Interested in multi-agent systems for different query types
        - Budget-conscious but willing to invest in high-ROI tools
        """
    }

    print("\nDesigning GraphRAG architecture...")
    result = graphrag_agent.run(**params)

    # Parse JSON result
    architecture = json.loads(result) if isinstance(result, str) else result

    print("\n" + "=" * 80)
    print("System Architecture:")
    print("=" * 80)
    components = architecture.get('architecture', {}).get('components', [])
    total_cost = architecture.get('architecture', {}).get('total_monthly_cost', 0)

    for component in components:
        print(f"\n{component.get('name')}")
        print(f"  Purpose: {component.get('purpose')}")
        print(f"  Deployment: {component.get('deployment')}")
        print(f"  Cost: ${component.get('cost_monthly')}/month")

    print(f"\nTotal Monthly Cost: ${total_cost}")

    print("\n" + "=" * 80)
    print("90-Day Implementation Roadmap:")
    print("=" * 80)
    roadmap = architecture.get('implementation_roadmap', {})
    for phase, details in roadmap.items():
        print(f"\n{phase}:")
        if isinstance(details, list):
            for task in details[:3]:  # Show first 3 tasks
                print(f"  - {task}")

    print("\n" + "=" * 80)
    print("ROI Projection:")
    print("=" * 80)
    roi = architecture.get('roi_projection', {})
    print(json.dumps(roi, indent=2))


# ==============================================================================
# Example 5: Sequential Agent Usage for Comprehensive Analysis
# ==============================================================================

def example_comprehensive_workflow():
    """
    Demonstrates using multiple agents in sequence for a comprehensive
    approach to AI freelancing transition.
    """
    print("\n" + "=" * 80)
    print("Example 5: Comprehensive Workflow (All Three Agents)")
    print("=" * 80)

    print("\n📊 Phase 1: Market Analysis (Revenue Extractor)")
    print("-" * 80)

    revenue_agent = Agent('montreal_revenue_extractor')
    revenue_result = revenue_agent.run(
        current_skills="Prompt engineering, AI automation",
        target_income=4000,
        available_hours=20,
        current_employment="Labatt operator",
        additional_context="Montreal-based, bilingual"
    )

    revenue_analysis = json.loads(revenue_result) if isinstance(revenue_result, str) else revenue_result
    niches = revenue_analysis.get('market_analysis', {}).get('underserved_niches', [])

    print(f"Found {len(niches)} potential niches")
    print(f"Top niche: {niches[0].get('niche') if niches else 'N/A'}")
    print(f"Rate range: {niches[0].get('rate_range') if niches else 'N/A'}")

    print("\n⚡ Phase 2: Productivity Optimization")
    print("-" * 80)

    productivity_agent = Agent('productivity_optimizer')
    productivity_result = productivity_agent.run(
        work_schedule="15:00-23:00",
        sleep_pattern="01:00-09:00",
        wake_time="09:00",
        energy_peaks="Morning, late afternoon",
        procrastination_triggers="Complex projects, admin tasks",
        primary_goal="Build freelance business",
        deep_work_hours=4
    )

    productivity_protocol = json.loads(productivity_result) if isinstance(productivity_result, str) else productivity_result
    optimal_windows = productivity_protocol.get('chronobiological_analysis', {}).get('optimal_work_windows', [])

    print(f"Identified {len(optimal_windows)} optimal work windows")
    if optimal_windows:
        print(f"Best deep work time: {optimal_windows[0].get('time')}")
        print(f"Ideal for: {', '.join(optimal_windows[0].get('ideal_tasks', []))}")

    print("\n🧠 Phase 3: Knowledge System Design")
    print("-" * 80)

    knowledge_agent = Agent('graphrag_architect')
    knowledge_result = knowledge_agent.run(
        data_sources=["Gmail", "Google Drive", "Notion", "GitHub"],
        document_count="60000",
        monthly_budget=500,
        use_cases=["Research past work", "Find AI techniques", "Generate prompts"]
    )

    knowledge_architecture = json.loads(knowledge_result) if isinstance(knowledge_result, str) else knowledge_result
    monthly_cost = knowledge_architecture.get('architecture', {}).get('total_monthly_cost', 0)
    time_saved = knowledge_architecture.get('roi_projection', {}).get('time_saved_monthly', 0)

    print(f"Architecture designed for ${monthly_cost}/month")
    print(f"Estimated time savings: {time_saved} hours/month")

    print("\n" + "=" * 80)
    print("📈 COMBINED ROI ANALYSIS")
    print("=" * 80)

    print(f"""
    Revenue Potential:
      - Target niches identified: {len(niches)}
      - Expected monthly income: ${revenue_analysis.get('revenue_projections', {}).get('monthly_income', 'N/A')}
      - Time to first client: {revenue_analysis.get('revenue_projections', {}).get('time_to_first_client', 'N/A')} days

    Productivity Gains:
      - Optimal work windows: {len(optimal_windows)} per day
      - Deep work capacity: {productivity_protocol.get('deep_work_architecture', {}).get('daily_capacity', 'N/A')} hours
      - Weekly time saved: ~{productivity_protocol.get('roi_projection', {}).get('weekly_time_saved', 'N/A')} hours

    Knowledge System:
      - Query latency: <2 seconds
      - Monthly time saved: {time_saved} hours
      - System cost: ${monthly_cost}/month
      - Annual ROI: {knowledge_architecture.get('roi_projection', {}).get('annual_roi_percentage', 'N/A')}%

    Total System Value:
      - Income increase potential: $4,000+/2 weeks
      - Time saved monthly: ~40 hours
      - System investment: ~${monthly_cost + 20}/month (knowledge + automation tools)
      - Net monthly value: $6,000+ (time + income)
      - Annual ROI: >10,000%
    """)


# ==============================================================================
# Main Execution
# ==============================================================================

if __name__ == "__main__":
    print("""
    ╔══════════════════════════════════════════════════════════════════════════╗
    ║                                                                          ║
    ║              ROI AUTOMATION SYSTEM - USAGE EXAMPLES                      ║
    ║                                                                          ║
    ║  A comprehensive AI-powered system for maximizing freelance income      ║
    ║  and productivity through intelligent automation.                       ║
    ║                                                                          ║
    ╚══════════════════════════════════════════════════════════════════════════╝

    This script demonstrates 5 different ways to use the system:

    1. Master Orchestration Cog (Recommended)
       → Automatic routing to the right specialist agent

    2. Montreal Revenue Extractor
       → Market analysis and client acquisition strategies

    3. Productivity Optimizer
       → Neuroscience-based performance enhancement

    4. GraphRAG Architect
       → Knowledge management system design

    5. Comprehensive Workflow
       → Using all agents together for maximum impact

    """)

    # Run examples (comment out any you don't want to run)
    try:
        # Example 1: Master cog (recommended for most use cases)
        example_master_cog()

        # Example 2: Direct agent usage examples
        # example_revenue_extractor()
        # example_productivity_optimizer()
        # example_graphrag_architect()

        # Example 5: Comprehensive workflow
        # example_comprehensive_workflow()

    except Exception as e:
        print(f"\n❌ Error running examples: {e}")
        print("\nMake sure you have:")
        print("  1. Installed AgentForge: pip install agentforge")
        print("  2. Configured API keys in .env or environment")
        print("  3. Copied the agent configurations to .agentforge/prompts/")
        print("  4. Copied the cog configuration to .agentforge/cogs/")
        print("\nSee docs/ROI_AUTOMATION_SYSTEM.md for setup instructions.")

    print("\n" + "=" * 80)
    print("Examples completed!")
    print("=" * 80)
    print("\nNext steps:")
    print("  1. Review the outputs above")
    print("  2. Customize the parameters for your specific situation")
    print("  3. Integrate into your workflow")
    print("  4. Track your ROI using the Google Sheets templates")
    print("\nFor more information, see: docs/ROI_AUTOMATION_SYSTEM.md")
    print("=" * 80)
