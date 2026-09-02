from client import AgentSessionReplayBehavioralAuditRecorderClient

def main():
    client = AgentSessionReplayBehavioralAuditRecorderClient()
    res = client.record_agent_session_trajectory('ses_demo_7721', [{'step': 1, 'act': 'BROWSE'}, {'step': 2, 'act': 'SUBMIT'}])
    print('Agent Session Replay Recorder: ' + res['recorded_session_id'] + ' (' + str(res['steps_logged_count']) + ' steps)')
    print('Oscillation Detected: ' + str(res['looping_oscillation_anomaly_detected']) + ' | Intent Fulfillment: ' + str(res['user_intent_fulfillment_score']))
    print('Replay Player URL: ' + res['interactive_session_replay_player_url'])

if __name__ == '__main__':
    main()
